import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder paths
RESUME_FOLDER = os.path.join(BASE_DIR, 'resumes')
PROCESSED_FOLDER = os.path.join(BASE_DIR, 'resumes', 'processed')
FAILED_FOLDER = os.path.join(BASE_DIR, 'resumes', 'failed')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output')

# Excel file path
EXCEL_FILE = os.path.join(OUTPUT_FOLDER, 'resume_data.xlsx')

# Monitoring settings
CHECK_INTERVAL = 5  # Check for new files every 5 seconds

# Supported file extensions
SUPPORTED_EXTENSIONS = ['.pdf', '.docx']

# Skills database
SKILLS_DB = [
    'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin',
    'go', 'rust', 'scala', 'r', 'matlab', 'sql', 'nosql', 'mongodb', 'postgresql', 'mysql',
    'oracle', 'redis', 'elasticsearch', 'cassandra', 'django', 'flask', 'fastapi', 'spring',
    'express', 'react', 'angular', 'vue', 'node.js', 'next.js', 'svelte', 'html', 'css',
    'sass', 'bootstrap', 'tailwind', 'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins',
    'git', 'github', 'gitlab', 'ci/cd', 'devops', 'linux', 'bash', 'terraform', 'ansible',
    'machine learning', 'deep learning', 'nlp', 'computer vision', 'tensorflow', 'pytorch',
    'keras', 'scikit-learn', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'opencv', 'transformers',
    'data analysis', 'data science', 'data engineering', 'etl', 'spark', 'hadoop', 'airflow',
    'tableau', 'power bi', 'excel', 'agile', 'scrum', 'jira', 'rest api', 'graphql', 'microservices',
    'unit testing', 'selenium', 'pytest', 'jest', 'junit', 'apis', 'web scraping'
]

def create_folders():
    """Create necessary folders if they don't exist"""
    folders = [RESUME_FOLDER, PROCESSED_FOLDER, FAILED_FOLDER, OUTPUT_FOLDER]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("✅ All folders created successfully!")