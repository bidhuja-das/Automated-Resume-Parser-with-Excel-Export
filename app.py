import os
import time
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

from config import (
    RESUME_FOLDER, PROCESSED_FOLDER, FAILED_FOLDER, 
    SUPPORTED_EXTENSIONS, CHECK_INTERVAL, create_folders
)
from resume_parser import parse_resume
from excel_handler import initialize_excel, append_to_excel, get_excel_stats

class ResumeHandler(FileSystemEventHandler):
    """Handle file system events"""
    
    def __init__(self):
        self.processed_files = set()
    
    def on_created(self, event):
        """Called when a file is created in the watched folder"""
        if event.is_directory:
            return
        
        file_path = event.src_path
        filename = os.path.basename(file_path)
        
        # Check if file has valid extension
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in SUPPORTED_EXTENSIONS:
            print(f"⚠️  Skipped (unsupported): {filename}")
            return
        
        # Avoid processing the same file multiple times
        if file_path in self.processed_files:
            return
        
        # Wait for file to be completely written
        time.sleep(2)
        
        # Check if file still exists (might be moved/deleted)
        if not os.path.exists(file_path):
            return
        
        self.processed_files.add(file_path)
        self.process_resume(file_path, filename)
    
    def process_resume(self, file_path, filename):
        """Process a single resume file"""
        print(f"\n{'='*60}")
        print(f"🔔 NEW RESUME DETECTED: {filename}")
        print(f"{'='*60}")
        
        try:
            # Parse the resume
            result = parse_resume(file_path, filename)
            
            if result:
                # Save to Excel
                if append_to_excel(result):
                    # Move to processed folder
                    destination = os.path.join(PROCESSED_FOLDER, filename)
                    
                    # Handle duplicate filenames
                    if os.path.exists(destination):
                        base, ext = os.path.splitext(filename)
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        destination = os.path.join(PROCESSED_FOLDER, f"{base}_{timestamp}{ext}")
                    
                    shutil.move(file_path, destination)
                    print(f"📁 Moved to: resumes/processed/")
                    print(f"✅ PROCESSING COMPLETE!")
                else:
                    raise Exception("Failed to write to Excel")
            else:
                raise Exception("Failed to parse resume")
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
            # Move to failed folder
            destination = os.path.join(FAILED_FOLDER, filename)
            
            # Handle duplicate filenames
            if os.path.exists(destination):
                base, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                destination = os.path.join(FAILED_FOLDER, f"{base}_{timestamp}{ext}")
            
            shutil.move(file_path, destination)
            print(f"📁 Moved to: resumes/failed/")
        
        print(f"{'='*60}\n")

def process_existing_files():
    """Process any existing files in the resume folder"""
    print("🔍 Checking for existing resumes...")
    
    files = [f for f in os.listdir(RESUME_FOLDER) 
             if os.path.isfile(os.path.join(RESUME_FOLDER, f))]
    
    resume_files = [f for f in files 
                   if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS]
    
    if resume_files:
        print(f"📋 Found {len(resume_files)} existing resume(s)")
        handler = ResumeHandler()
        for filename in resume_files:
            file_path = os.path.join(RESUME_FOLDER, filename)
            handler.process_resume(file_path, filename)
    else:
        print("✅ No existing resumes to process")

def main():
    """Main function to run the automation"""
    print("\n" + "="*60)
    print("🤖 AUTOMATED RESUME PARSER SYSTEM")
    print("="*60 + "\n")
    
    # Create folders
    print("📁 Setting up folders...")
    create_folders()
    
    # Initialize Excel
    print("\n📊 Setting up Excel file...")
    initialize_excel()
    
    # Show current stats
    total_records = get_excel_stats()
    print(f"📈 Total records in Excel: {total_records}")
    
    # Process existing files
    print("\n" + "-"*60)
    process_existing_files()
    print("-"*60)
    
    # Start monitoring
    print("\n👀 MONITORING STARTED...")
    print(f"📂 Watching folder: {RESUME_FOLDER}")
    print(f"⏱️  Check interval: {CHECK_INTERVAL} seconds")
    print("\n💡 Instructions:")
    print("   1. Drop your resume (PDF/DOCX) in the 'resumes/' folder")
    print("   2. The system will automatically process it")
    print("   3. Check 'output/resume_data.xlsx' for extracted data")
    print("   4. Processed files move to 'resumes/processed/'")
    print("   5. Failed files move to 'resumes/failed/'")
    print("\n⚠️  Press Ctrl+C to stop monitoring\n")
    print("="*60 + "\n")
    
    # Set up file system observer
    event_handler = ResumeHandler()
    observer = Observer()
    observer.schedule(event_handler, RESUME_FOLDER, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping monitoring...")
        observer.stop()
        observer.join()
        print("✅ System stopped successfully!")
        print(f"📊 Final count: {get_excel_stats()} records processed")
        print("\nThank you for using Automated Resume Parser! 👋\n")

if __name__ == "__main__":
    main()
