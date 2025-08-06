import subprocess

def install_requirements():
    print("📦 Installing dependencies from requirements.txt...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed.")

if __name__ == "__main__":
    install_requirements()
    print("🚀 Setup complete!")