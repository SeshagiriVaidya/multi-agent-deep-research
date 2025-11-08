"""
Quick setup script for Multi-Agent AI Deep Researcher
"""

import os
import subprocess
import sys

def create_env_file():
    """Create .env file from template if it doesn't exist."""
    if not os.path.exists('.env'):
        env_content = """# OpenAI API Key (required)
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Other API keys
# ANTHROPIC_API_KEY=your_anthropic_api_key_here
# NEWS_API_KEY=your_news_api_key_here
"""
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Created .env file. Please add your OPENAI_API_KEY")
    else:
        print("✅ .env file already exists")

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def main():
    """Main setup function."""
    print("🚀 Setting up Multi-Agent AI Deep Researcher...")
    print()
    
    create_env_file()
    print()
    
    install_dependencies()
    print()
    
    print("✅ Setup complete!")
    print()
    print("Next steps:")
    print("1. Edit .env file and add your OPENAI_API_KEY")
    print("2. Run: streamlit run app.py")
    print()

if __name__ == "__main__":
    main()

