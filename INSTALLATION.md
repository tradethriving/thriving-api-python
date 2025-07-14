# Installation Guide

This guide covers installation and setup of the Thriving API Python SDK.

## Requirements

- Python 3.10 or higher
- pip (Python package installer)
- A Thriving API key (get one at [tradethriving.com](https://tradethriving.com/api-dashboard))

## Installation Methods

### 1. Install from PyPI (Recommended)

```bash
pip install thriving-api
```

### 2. Install from Source

```bash
# Clone the repository
git clone https://github.com/thriving/thriving-api-python.git
cd thriving-api-python

# Install in development mode
pip install -e .

# Or install normally
pip install .
```

### 3. Install with Development Dependencies

```bash
# For contributors and developers
pip install thriving-api[dev]

# Or from source
pip install -e ".[dev]"
```

## Verify Installation

```python
import thriving_api
print(f"Thriving API SDK version: {thriving_api.__version__}")

# Test basic import
from thriving_api import ThrivingAPI
print("✅ Installation successful!")
```

## API Key Setup

### Method 1: Environment Variable (Recommended)

```bash
# Linux/macOS
export THRIVING_API_KEY="your-api-key-here"

# Windows
set THRIVING_API_KEY=your-api-key-here

# Or add to your .bashrc/.zshrc
echo 'export THRIVING_API_KEY="your-api-key-here"' >> ~/.bashrc
```

### Method 2: .env File

Create a `.env` file in your project root:

```env
THRIVING_API_KEY=your-api-key-here
```

Then load it in your Python code:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("THRIVING_API_KEY")
```

### Method 3: Direct in Code (Not Recommended for Production)

```python
from thriving_api import ThrivingAPI

client = ThrivingAPI(api_key="your-api-key-here")
```

## Quick Test

```python
import asyncio
import os
from thriving_api import ThrivingAPI

async def test_connection():
    api_key = os.getenv("THRIVING_API_KEY")
    if not api_key:
        print("❌ Please set THRIVING_API_KEY environment variable")
        return
    
    try:
        async with ThrivingAPI(api_key=api_key) as client:
            # Test with a simple market status call
            status = await client.market.get_status()
            print("✅ Connection successful!")
            print(f"Found {len(status.markets)} markets")
            
            # Test AI analysis
            analysis = await client.ai.analyze_symbol("AAPL")
            print(f"✅ AI analysis successful!")
            print(f"AAPL recommendation: {analysis.analysis.action}")
            
    except Exception as e:
        print(f"❌ Connection failed: {e}")

# Run the test
asyncio.run(test_connection())
```

## Virtual Environment Setup (Recommended)

### Using venv

```bash
# Create virtual environment
python -m venv thriving-env

# Activate (Linux/macOS)
source thriving-env/bin/activate

# Activate (Windows)
thriving-env\Scripts\activate

# Install SDK
pip install thriving-api

# Deactivate when done
deactivate
```

### Using conda

```bash
# Create environment
conda create -n thriving python=3.10

# Activate
conda activate thriving

# Install SDK
pip install thriving-api

# Deactivate when done
conda deactivate
```

## Troubleshooting

### Common Issues

#### 1. Import Error

```
ImportError: No module named 'thriving_api'
```

**Solution:**
- Ensure you've installed the package: `pip install thriving-api`
- Check you're in the correct virtual environment
- Verify Python version: `python --version` (should be 3.10+)

#### 2. Authentication Error

```
AuthenticationError: Invalid or missing API key
```

**Solution:**
- Verify your API key is correct
- Check environment variable is set: `echo $THRIVING_API_KEY`
- Ensure no extra spaces or characters in the key

#### 3. Connection Error

```
APIConnectionError: Failed to connect to API
```

**Solution:**
- Check internet connection
- Verify API endpoint is accessible: `curl https://ai.tradethriving.com/markets/status`
- Check firewall/proxy settings

#### 4. Rate Limit Error

```
RateLimitError: Rate limit exceeded
```

**Solution:**
- Wait before making more requests
- Enable rate limiting: `ThrivingAPI(api_key="...", enable_rate_limiting=True)`
- Reduce request frequency

#### 5. SSL Certificate Error

```
SSLError: certificate verify failed
```

**Solution:**
- Update certificates: `pip install --upgrade certifi`
- Check system time is correct
- Try with custom SSL context if needed

### Getting Help

1. **Check Documentation**: [docs.tradethriving.com/api](https://docs.tradethriving.com/api)
2. **GitHub Issues**: [github.com/thriving/thriving-api-python/issues](https://github.com/thriving/thriving-api-python/issues)
3. **Email Support**: [support@tradethriving.com](mailto:support@tradethriving.com)

### Debug Mode

Enable debug logging to troubleshoot issues:

```python
import logging
from thriving_api import ThrivingAPI

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Create client with debug info
client = ThrivingAPI(api_key="your-api-key")

# Check client stats
stats = client.get_stats()
print(f"Client stats: {stats}")

# Check rate limiting
rate_info = client.get_rate_limit_info()
print(f"Rate limit info: {rate_info}")
```

## Next Steps

1. **Read the Documentation**: Check out the [README.md](README.md) for usage examples
2. **Explore Examples**: Look at the `examples/` directory for comprehensive examples
3. **API Reference**: Visit [docs.tradethriving.com/api](https://docs.tradethriving.com/api) for detailed API documentation
4. **Join the Community**: Follow updates and get support through our channels

## Development Setup

For contributors and advanced users:

```bash
# Clone repository
git clone https://github.com/thriving/thriving-api-python.git
cd thriving-api-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in development mode
pip install -e .

# Run tests
pytest

# Run linting
black src/
isort src/
flake8 src/
mypy src/

# Build documentation
cd docs/
make html
```
