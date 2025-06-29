#!/bin/bash

set -e

OS="$(uname -s)"

echo "=== Hudl Test Automation Setup ==="
echo "This script will install all dependencies needed for running tests."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
  echo "Python3 is not installed. Please install Python 3.x."
  exit 1
fi

# Check pip
if ! command -v pip3 &> /dev/null; then
  echo "pip3 is not installed. Please install pip for Python 3."
  exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt
echo "[OK] Python dependencies installed."

# Check Java
if ! command -v java &> /dev/null; then
  echo "Java (JRE) is not installed or not in PATH. Attempting to install..."
  if [[ "$OS" == "Darwin" ]]; then
    if ! command -v brew &> /dev/null; then
      echo "Homebrew not found. Installing Homebrew..."
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      eval "$($(brew --prefix)/bin/brew shellenv)"
    fi
    brew install openjdk
    sudo ln -sfn $(brew --prefix openjdk)/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
    echo 'export PATH="$(brew --prefix openjdk)/bin:$PATH"' >> ~/.zshrc
    export PATH="$(brew --prefix openjdk)/bin:$PATH"
  elif [[ "$OS" == "Linux" ]]; then
    if command -v apt &> /dev/null; then
      sudo apt update && sudo apt install -y openjdk-11-jre
    else
      echo "Please install Java manually (OpenJDK 11+)."
    fi
  elif [[ "$OS" =~ MINGW|MSYS|CYGWIN ]]; then
    if ! command -v choco &> /dev/null; then
      echo "Please install Chocolatey from https://chocolatey.org/install and rerun this script."
      exit 1
    fi
    choco install openjdk --version=11.0.2
  else
    echo "Unknown OS. Please install Java manually."
  fi
else
  echo "[OK] Java is installed."
fi

# Check Allure commandline
if ! command -v allure &> /dev/null; then
  echo "Allure commandline is not installed or not in PATH. Attempting to install..."
  if [[ "$OS" == "Darwin" ]]; then
    if ! command -v brew &> /dev/null; then
      echo "Homebrew not found. Installing Homebrew..."
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      eval "$($(brew --prefix)/bin/brew shellenv)"
    fi
    brew install allure
  elif [[ "$OS" == "Linux" ]]; then
    LATEST_URL=$(curl -s https://api.github.com/repos/allure-framework/allure2/releases/latest | grep browser_download_url | grep tgz | cut -d '"' -f 4)
    wget "$LATEST_URL" -O allure-latest.tgz
    tar -zxvf allure-latest.tgz
    sudo mv allure-* /opt/allure
    sudo ln -sf /opt/allure/bin/allure /usr/bin/allure
    rm allure-latest.tgz
  elif [[ "$OS" =~ MINGW|MSYS|CYGWIN ]]; then
    if ! command -v scoop &> /dev/null; then
      echo "Scoop not found. Installing Scoop..."
      powershell -Command "Set-ExecutionPolicy RemoteSigned -scope CurrentUser; iwr -useb get.scoop.sh | iex"
      export PATH="$PATH:$HOME/scoop/shims"
    fi
    scoop install allure
  else
    echo "Unknown OS. Please install Allure manually."
  fi
else
  echo "[OK] Allure commandline is installed."
fi

# Check Docker
if ! command -v docker &> /dev/null; then
  echo "Docker is not installed. Attempting to install..."
  if [[ "$OS" == "Darwin" ]]; then
    if ! command -v brew &> /dev/null; then
      echo "Homebrew not found. Installing Homebrew..."
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      eval "$($(brew --prefix)/bin/brew shellenv)"
    fi
    echo "Installing Docker Desktop via Homebrew..."
    brew install --cask docker
    echo "Docker Desktop installed. Please start Docker Desktop from Applications folder."
    echo "After starting Docker Desktop, you may need to restart your terminal."
  elif [[ "$OS" == "Linux" ]]; then
    echo "Installing Docker on Linux..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    rm get-docker.sh
    echo "Docker installed. You may need to log out and back in for group changes to take effect."
  elif [[ "$OS" =~ MINGW|MSYS|CYGWIN ]]; then
    echo "For Windows, please install Docker Desktop manually:"
    echo "https://www.docker.com/products/docker-desktop"
    echo "After installation, restart your terminal."
  else
    echo "Unknown OS. Please install Docker manually:"
    echo "https://www.docker.com/products/docker-desktop"
  fi
else
  echo "[OK] Docker is installed."
fi

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "Your environment is now ready for running tests."
echo ""
echo "=== Quick Start ==="
echo "1. Run tests (headless mode by default):"
echo "   pytest"
echo ""
echo "2. Run tests with browser window visible:"
echo "   HEADLESS=false pytest"
echo ""
echo "3. Run tests with different browser:"
echo "   pytest --browser=firefox"
echo ""
echo "4. Generate HTML report:"
echo "   pytest --html=report.html --self-contained-html"
echo ""
echo "5. Generate Allure report:"
echo "   pytest --alluredir=allure-results"
echo "   allure serve allure-results"
echo ""
echo "6. Run in Docker (if Docker is installed and running):"
echo "   docker build -t hudl-tests ."
echo "   docker run --rm hudl-tests"
echo ""
echo "=== Headless Mode ==="
echo "• Tests run in headless mode by default (no browser window)"
echo "• To show browser window: HEADLESS=false pytest"
echo "• To explicitly enable headless: HEADLESS=true pytest"
echo ""
echo "For more information, see the README.md file." 