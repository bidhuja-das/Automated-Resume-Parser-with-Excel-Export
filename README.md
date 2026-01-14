# Automated-Resume-Parser-with-Excel-Export
An intelligent, production-ready automation system that monitors a designated folder for resume uploads and automatically extracts candidate information using Machine Learning and Natural Language Processing. The extracted data is seamlessly appended to an Excel spreadsheet with timestamps, making recruitment and candidate tracking effortless.

✨ Key Features

🔍 Real-Time Monitoring: Continuously watches the resumes/ folder using Python's Watchdog library
🤖 AI-Powered Extraction: Leverages spaCy's Named Entity Recognition (NER) for intelligent data extraction
📊 Automatic Excel Updates: Appends extracted data to Excel with timestamps - no manual intervention required
📁 Smart File Management: Automatically organizes processed and failed resumes into separate folders
⚡ Instant Processing: Processes resumes within 2-3 seconds of upload
🔄 Batch Processing: Handles existing files on startup and processes them automatically
💼 Multi-Format Support: Works with both PDF and DOCX resume formats
🎯 Comprehensive Data Extraction:

Full Name (using spaCy NER)
Email Address (regex pattern matching)
Phone Number (multiple format support)
Technical Skills (60+ predefined skills database)



🏗️ Architecture
resume-automation/
│
├── app.py                      # Main automation engine with file monitoring
├── resume_parser.py            # ML-based parsing logic (spaCy + Regex)
├── excel_handler.py            # Excel operations with openpyxl
├── config.py                   # Centralized configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
│
├── resumes/                    # Drop resumes here (auto-monitored)
│   ├── processed/              # Successfully processed resumes
│   └── failed/                 # Failed processing attempts
│
└── output/
    └── resume_data.xlsx        # Auto-generated Excel with extracted data
🚀 How It Works

Upload: Drop a resume (PDF/DOCX) into the resumes/ folder
Detection: Watchdog library detects the new file instantly
Extraction: spaCy NER and regex extract name, email, phone, and skills
Excel Update: Data is automatically appended to resume_data.xlsx with timestamp
Organization: Processed file moves to resumes/processed/ folder
Ready: System continues monitoring for the next resume

🛠️ Technology Stack

Python 3.8+ - Core programming language
spaCy - Natural Language Processing for name extraction
PyMuPDF (fitz) - PDF text extraction
python-docx - DOCX text extraction
openpyxl - Excel file manipulation
Watchdog - File system event monitoring
Regex - Pattern matching for email and phone numbers

📦 Installation
Prerequisites

Python 3.8 or higher
pip package manager

Setup
bash# Clone the repository
git clone https://github.com/bidhuja_das/Automated-Resume-Parser_with_excel_Export.git
cd Automated-Resume-Parser_with_excel_Export

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy language model
python -m spacy download en_core_web_sm
💻 Usage
Start the Automation System
bashpython app.py
Process Resumes

System creates necessary folders automatically
Drop resume files (PDF or DOCX) into the resumes/ folder
Watch the terminal for real-time processing status
Check output/resume_data.xlsx for extracted data
Processed resumes are moved to resumes/processed/

Stop the System
Press Ctrl + C in the terminal
📊 Excel Output Format
Sr. No.Date & TimeFile NameNameEmailPhoneSkills12025-01-14 10:30:00john_doe.pdfJohn Doejohn@email.com+1-234-567-8900python, django, aws, docker22025-01-14 10:31:15jane_smith.docxJane Smithjane@email.com+1-987-654-3210java, spring, kubernetes
🎯 Use Cases

Recruitment Teams: Automatically process hundreds of resumes
HR Departments: Build candidate databases effortlessly
Staffing Agencies: Quick candidate information extraction
Job Portals: Backend automation for resume parsing
Academic Research: Analyze resume trends and patterns

🔧 Configuration
Customize the system by editing config.py:
python# Monitoring interval (seconds)
CHECK_INTERVAL = 5

# Add custom skills to the database
SKILLS_DB = [
    'python', 'java', 'javascript',
    'your-custom-skill',  # Add here
]

# Change folder paths
RESUME_FOLDER = 'path/to/your/folder'
📈 Performance

⚡ Processes 1 resume in ~2-3 seconds
📁 Handles multiple files sequentially
📄 Supports resumes up to 10+ pages
💾 Low memory footprint (~100MB)
🔄 Can process 1000+ resumes without issues

🛡️ Error Handling

Invalid Format: Unsupported files are skipped with warnings
Parsing Failures: Failed resumes move to resumes/failed/ folder
Excel Locked: System waits if Excel file is open
Duplicate Names: Automatically adds timestamps to avoid conflicts

🔒 Security & Privacy

✅ All processing happens locally (no external API calls)
✅ No data sent to cloud services
✅ Files are moved, not deleted (data preservation)
✅ Secure file handling with proper validation

🐛 Troubleshooting
spaCy model not found
bashpython -m spacy download en_core_web_sm
Excel file is locked
Close the Excel file before processing resumes
Permission denied errors
Run terminal as Administrator (Windows) or use sudo (macOS/Linux)
No text extracted from PDF
Ensure PDF contains selectable text (not scanned images)
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 Future Enhancements

 Support for more file formats (DOC, RTF, TXT)
 Education and work experience extraction
 Multi-language resume support
 Web dashboard for monitoring
 REST API for remote access
 Database integration (PostgreSQL/MongoDB)
 Resume quality scoring
 Duplicate candidate detection
 Email notifications on processing
 Advanced ML models (BERT, Transformers)

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Author
Your Name

GitHub: @yourusername
LinkedIn: Your LinkedIn
Email: your.email@example.com

🙏 Acknowledgments

spaCy - Industrial-strength NLP
openpyxl - Excel file manipulation
Watchdog - File system monitoring
PyMuPDF - PDF processing

⭐ Support
If you find this project helpful, please give it a ⭐ on GitHub!
📧 Contact
For questions, suggestions, or support:

Open an issue on GitHub
Email: your.email@example.com
Twitter: @yourhandle


Made with ❤️ and Python

🎯 Quick Start Guide
bash# 1. Clone and setup
git clone https://github.com/yourusername/resume-automation.git
cd resume-automation
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 2. Run the system
python app.py

# 3. Drop resumes in resumes/ folder and watch the magic! ✨
```

## 📸 Screenshots

### Terminal Output
```
============================================================
🤖 AUTOMATED RESUME PARSER SYSTEM
============================================================

📁 Setting up folders...
✅ All folders created successfully!

📊 Setting up Excel file...
✅ Excel file created successfully!

👀 MONITORING STARTED...
📂 Watching folder: /path/to/resumes
⏱️  Check interval: 5 seconds

============================================================
🔔 NEW RESUME DETECTED: john_doe_resume.pdf
============================================================
📄 Processing: john_doe_resume.pdf
✅ Successfully parsed: john_doe_resume.pdf
✅ Data added to Excel (Row 1)
📁 Moved to: resumes/processed/
✅ PROCESSING COMPLETE!
============================================================

Happy Automating! 🚀
