import re
import spacy
import fitz  # PyMuPDF
from docx import Document
from config import SKILLS_DB

# Load spaCy model
try:
    nlp = spacy.load('en_core_web_sm')
except:
    print("📥 Downloading spaCy model...")
    import os
    os.system('python -m spacy download en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(file_path):
    """Extract text from PDF using PyMuPDF"""
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"❌ Error extracting PDF: {e}")
        return None

def extract_text_from_docx(file_path):
    """Extract text from DOCX"""
    try:
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"❌ Error extracting DOCX: {e}")
        return None

def extract_name(text):
    """Extract name using multiple strategies"""
    try:
        # Strategy 1: spaCy NER for PERSON entities
        doc = nlp(text[:2000])
        
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                name = ent.text.strip()
                # Filter out common non-person patterns
                if (len(name.split()) >= 1 and len(name.split()) <= 4 and 
                    not any(word in name.lower() for word in ['artificial', 'intelligence', 'machine', 'learning', 'data', 'science', 'engineering', 'curriculum', 'vitae', 'resume']) and
                    len(name) < 50 and
                    not name.isdigit() and
                    not any(char.isdigit() for char in name) and
                    not name.lower().startswith('http') and
                    '@' not in name.lower()):
                    return name
        
        # Strategy 2: Look for capitalized names at the beginning
        lines = text.split('\n')[:15]  # Check first 15 lines
        for i, line in enumerate(lines):
            line = line.strip()
            if line and len(line) < 50:
                # Skip common headers/titles
                skip_words = ['resume', 'curriculum', 'vitae', 'cv', 'contact', 'phone', 'email', 'address', 'objective', 'summary', 'experience', 'education', 'skills']
                if any(skip_word in line.lower() for skip_word in skip_words):
                    continue
                
                # Check for name patterns
                words = line.split()
                if 1 <= len(words) <= 4:
                    # All words should start with capital letter (except possible abbreviations)
                    capitalized_words = 0
                    for word in words:
                        if word and (word[0].isupper() or word.isupper()):
                            capitalized_words += 1
                    
                    # If at least 70% of words are capitalized, consider it a name
                    if capitalized_words >= len(words) * 0.7:
                        # Additional validation: no digits, no @ symbol
                        if not any(char.isdigit() for char in line) and '@' not in line:
                            return line
        
        # Strategy 3: Look for single capitalized words (like "Nandana")
        for line in lines[:10]:
            line = line.strip()
            if (line and len(line.split()) == 1 and 
                len(line) > 2 and len(line) < 30 and
                line[0].isupper() and 
                not any(char.isdigit() for char in line) and
                '@' not in line and
                not line.lower() in ['resume', 'cv', 'name', 'objective', 'summary']):
                return line
        
        # Strategy 4: Look for patterns like "Name: John Doe" or "I am John Doe"
        import re
        name_patterns = [
            r'(?:name|called|am|is)\s+[:\-]?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})',
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\s*$',
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\n+',
        ]
        
        for pattern in name_patterns:
            matches = re.findall(pattern, text[:1000], re.MULTILINE | re.IGNORECASE)
            if matches:
                for match in matches:
                    match = match.strip()
                    if len(match.split()) <= 4 and len(match) < 50:
                        return match
        
        return "Not Found"
    except Exception as e:
        print(f"Name extraction error: {e}")
        return "Not Found"

def extract_email(text):
    """Extract email using regex"""
    try:
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return emails[0] if emails else "Not Found"
    except:
        return "Not Found"

def extract_phone(text):
    """Extract phone number using regex"""
    try:
        phone_patterns = [
            r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            r'\d{10}',
            r'\+\d{11,12}'
        ]
        for pattern in phone_patterns:
            phones = re.findall(pattern, text)
            if phones:
                return phones[0]
        return "Not Found"
    except:
        return "Not Found"

def extract_skills(text):
    """Extract skills using keyword matching"""
    try:
        text_lower = text.lower()
        found_skills = []
        for skill in SKILLS_DB:
            if skill in text_lower:
                if skill not in found_skills:
                    found_skills.append(skill)
        return ', '.join(found_skills) if found_skills else "No skills detected"
    except:
        return "No skills detected"

def parse_resume(file_path, filename):
    """Main parsing function"""
    print(f"📄 Processing: {filename}")
    
    # Extract text based on file type
    if filename.lower().endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif filename.lower().endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        print(f"❌ Unsupported file type: {filename}")
        return None
    
    if not text:
        print(f"❌ Failed to extract text from: {filename}")
        return None
    
    # Extract information
    result = {
        'filename': filename,
        'name': extract_name(text),
        'email': extract_email(text),
        'phone': extract_phone(text),
        'skills': extract_skills(text)
    }
    
    print(f"✅ Successfully parsed: {filename}")
    return result