#!/bin/bash

set -e

OS="$(uname -s)"

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

echo "\nSetup complete! You can now run tests and generate reports." 