# Thriving API Python SDK

[![PyPI version](https://badge.fury.io/py/thriving-api.svg)](https://badge.fury.io/py/thriving-api)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python SDK for the **Thriving API** - Your gateway to institutional-grade financial analysis and AI-powered trading intelligence.

## 🚀 Features

- **AI-Powered Analysis**: Get buy/sell/hold recommendations with confidence scores
- **Real-Time Market Data**: Live quotes, OHLC data, and market status
- **Technical Indicators**: 50+ technical analysis tools (RSI, MACD, Bollinger Bands, etc.)
- **Company Fundamentals**: Financial statements, earnings, and key metrics
- **Options Data**: Complete options chains with Greeks and implied volatility
- **News & Sentiment**: Latest news with AI-powered sentiment analysis
- **Rate Limiting**: Intelligent rate limiting with adaptive behavior
- **Error Handling**: Comprehensive error handling and retry logic
- **Type Safety**: Full type hints and Pydantic validation
- **Async Support**: Built for high-performance async applications

## 📦 Installation

```bash
pip install thriving-api
```

## 🔑 Authentication

Get your API key from the [Thriving API Dashboard](https://tradethriving.com/api-dashboard).

```python
from thriving_api import ThrivingAPI

# Initialize client
client = ThrivingAPI(api_key="your-api-key")
```

## 🏃 Quick Start

### AI-Powered Stock Analysis

```python
import asyncio
from thriving_api import ThrivingAPI

async def analyze_stock():
    async with ThrivingAPI(api_key="your-api-key") as client:
        # Get AI analysis for Apple
        analysis = await client.ai.analyze_symbol("AAPL")
        
        print(f"Symbol: {analysis.analysis.symbol}")
        print(f"Action: {analysis.analysis.action}")  # buy, sell, or wait
        print(f"Confidence: {analysis.analysis.get_confidence_percentage():.1f}%")
        print(f"Trade Score: {analysis.analysis.trade_score:.1f}/100")
        
        if analysis.analysis.optimal_stop_loss:
            print(f"Stop Loss: ${analysis.analysis.optimal_stop_loss:.2f}")

# Run the analysis
asyncio.run(analyze_stock())
```

### Symbol Search and Market Data

```python
async def get_market_data():
    async with ThrivingAPI(api_key="your-api-key") as client:
        # Search for symbols
        search_results = await client.symbol.search("Apple")
        best_match = search_results.results.get_best_match()
        print(f"Best match: {best_match.symbol} - {best_match.name}")
        
        # Get live quote
        quote = await client.symbol.get_live_quote("AAPL", "1min")
        latest = quote.get_latest_quote()
        print(f"Current price: ${latest.get_close():.2f}")
        print(f"Volume: {latest.get_volume():,}")
        
        # Get performance
        performance = await client.symbol.get_performance("AAPL", "1yr")
        yearly_return = performance.get_performance_float("1yr")
        print(f"1-year return: {yearly_return:.2f}%")

asyncio.run(get_market_data())
```

### Company Fundamentals

```python
async def get_fundamentals():
    async with ThrivingAPI(api_key="your-api-key") as client:
        # Get company fundamentals
        fundamentals = await client.company.get_fundamentals("AAPL")
        company = fundamentals.fundamentals
        
        print(f"P/E Ratio: {company.get_pe_ratio()}")
        print(f"Market Cap: ${company.get_market_cap():,}")
        print(f"Debt/Equity: {company.get_debt_to_equity()}")
        print(f"Dividend Yield: {company.get_dividend_yield_percent():.2f}%")
        
        # Get financial strength score
        strength = company.get_financial_strength_score()
        if strength:
            print(f"Financial Strength: {strength:.1f}/100")

asyncio.run(get_fundamentals())
```

### Technical Analysis

```python
async def technical_analysis():
    async with ThrivingAPI(api_key="your-api-key") as client:
        # Get RSI
        rsi = await client.technical.get_rsi("AAPL", "daily", 14)
        current_rsi = rsi.get_current_signal()
        print(f"RSI Signal: {current_rsi}")
        
        # Get MACD
        macd = await client.technical.get_macd("AAPL", "daily")
        macd_signal = macd.get_current_signal()
        print(f"MACD Signal: {macd_signal}")
        
        # Get Bollinger Bands
        bbands = await client.technical.get_bollinger_bands("AAPL", "daily", 20)
        latest_bands = bbands.get_latest_bands()
        if latest_bands:
            print(f"Upper Band: ${latest_bands.get_upper_band():.2f}")
            print(f"Lower Band: ${latest_bands.get_lower_band():.2f}")

asyncio.run(technical_analysis())
```

## 📚 API Modules

The SDK is organized into specialized modules for different types of data:

### 🤖 AI Module (`client.ai`)
- `analyze_symbol(symbol)` - Get AI trading recommendations
- `analyze_symbol_with_data(symbol, custom_data)` - Enhanced analysis with custom data

### 📈 Symbol Module (`client.symbol`)
- `search(query)` - Search for stock symbols
- `get_performance(symbol, interval)` - Get performance metrics
- `get_live_quote(symbol, interval)` - Get real-time quotes
- `get_ohlc_daily(symbol)` - Get daily OHLC data
- `get_news(symbol)` - Get latest news and sentiment

### 🏢 Company Module (`client.company`)
- `get_fundamentals(symbol)` - Get financial fundamentals
- `get_earnings(symbol)` - Get earnings data
- `get_details(symbol)` - Get company profile

### 📊 Technical Module (`client.technical`)
- `get_sma(symbol, interval, period)` - Simple Moving Average
- `get_ema(symbol, interval, period)` - Exponential Moving Average
- `get_rsi(symbol, interval, period)` - Relative Strength Index
- `get_macd(symbol, interval)` - MACD indicator
- `get_bollinger_bands(symbol, interval, period)` - Bollinger Bands
- `get_stochastic(symbol, interval)` - Stochastic Oscillator
- And 40+ more technical indicators...

### 📋 Options Module (`client.options`)
- `get_chain(symbol)` - Get complete options chain
- `get_contract_details(symbol, contract)` - Get specific contract details

### 🏪 Market Module (`client.market`)
- `get_status()` - Get market status and trading hours

## ⚙️ Configuration

### Rate Limiting

The SDK includes intelligent rate limiting to prevent API quota exhaustion:

```python
client = ThrivingAPI(
    api_key="your-api-key",
    requests_per_second=30,  # Default rate limit
    burst_limit=60,          # Burst capacity
    enable_rate_limiting=True # Enable client-side limiting
)

# Check rate limit status
rate_info = client.get_rate_limit_info()
print(f"Current rate: {rate_info['current_rate']} req/sec")
```

### Error Handling

The SDK provides comprehensive error handling:

```python
from thriving_api import (
    ThrivingAPI, 
    AuthenticationError, 
    RateLimitError, 
    ValidationError,
    SymbolNotFoundError
)

async def handle_errors():
    try:
        async with ThrivingAPI(api_key="your-api-key") as client:
            analysis = await client.ai.analyze_symbol("INVALID")
    except AuthenticationError:
        print("Invalid API key")
    except SymbolNotFoundError as e:
        print(f"Symbol not found: {e.symbol}")
    except RateLimitError as e:
        print(f"Rate limited. Retry after: {e.retry_after} seconds")
    except ValidationError as e:
        print(f"Validation error: {e.message}")

asyncio.run(handle_errors())
```

### Timeouts and Retries

```python
client = ThrivingAPI(
    api_key="your-api-key",
    timeout=60.0,      # Request timeout in seconds
    max_retries=5      # Maximum retry attempts
)
```

## 📊 Response Models

All API responses are validated using Pydantic models with full type safety:

```python
# AI Analysis Response
analysis: AIAnalysisResponse = await client.ai.analyze_symbol("AAPL")
print(analysis.analysis.action)           # Typed as Literal["buy", "sell", "wait"]
print(analysis.analysis.confidence)       # Typed as float
print(analysis.analysis.trade_score)      # Typed as float

# Symbol Search Response  
results: SymbolSearchResponse = await client.symbol.search("AAPL")
matches: List[SymbolMatch] = results.results.matches

# Technical Indicator Response
rsi: RSIResponse = await client.technical.get_rsi("AAPL", "daily", 14)
latest_rsi: Optional[RSIDataPoint] = rsi.get_latest_rsi()
```

## 🔧 Advanced Usage

### Custom HTTP Client Configuration

```python
client = ThrivingAPI(
    api_key="your-api-key",
    base_url="https://custom-api-url.com",  # Custom base URL
    timeout=120.0,                          # Extended timeout
    max_retries=10,                         # More retries
    requests_per_second=50,                 # Higher rate limit
)
```

### Batch Operations

```python
async def batch_analysis():
    symbols = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]
    
    async with ThrivingAPI(api_key="your-api-key") as client:
        # Analyze multiple symbols concurrently
        tasks = [client.ai.analyze_symbol(symbol) for symbol in symbols]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for symbol, result in zip(symbols, results):
            if isinstance(result, Exception):
                print(f"Error analyzing {symbol}: {result}")
            else:
                print(f"{symbol}: {result.analysis.action} (Score: {result.analysis.trade_score:.1f})")

asyncio.run(batch_analysis())
```

### Statistics and Monitoring

```python
# Get client statistics
stats = client.get_stats()
print(f"Total requests: {stats['total_requests']}")
print(f"Successful requests: {stats['successful_requests']}")
print(f"Failed requests: {stats['failed_requests']}")
print(f"Rate limited requests: {stats['rate_limited_requests']}")

# Get rate limiting info
rate_info = client.get_rate_limit_info()
print(f"Available tokens: {rate_info['available_tokens']}")
print(f"Requests per minute: {rate_info['recent_requests_per_minute']}")

## 🧪 Testing

The SDK includes comprehensive test coverage. To run tests:

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=thriving_api --cov-report=html
```

## 📖 Examples

Check out the `examples/` directory for more comprehensive examples:

- `basic_usage.py` - Basic SDK usage patterns
- `ai_analysis.py` - AI analysis examples
- `technical_indicators.py` - Technical analysis examples
- `portfolio_analysis.py` - Portfolio-level analysis
- `options_analysis.py` - Options trading examples
- `news_sentiment.py` - News and sentiment analysis

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [https://tradethriving.com/api-documentation](https://tradethriving.com/api-documentation)
- **API Dashboard**: [https://tradethriving.com/api-dashboard](https://tradethriving.com/api-dashboard)
- **Email Support**: [support@tradethriving.com](mailto:support@tradethriving.com)
- **GitHub Issues**: [Report bugs and request features](https://github.com/thriving/thriving-api-python/issues)

## 🔗 Links

- **Homepage**: [https://tradethriving.com](https://tradethriving.com)
- **API Documentation**: [https://tradethriving.com/api-documentation](https://tradethriving.com/api-documentation)
- **PyPI Package**: [https://pypi.org/project/thriving-api/](https://pypi.org/project/thriving-api/)
- **GitHub Repository**: [https://github.com/thriving/thriving-api-python](https://github.com/thriving/thriving-api-python)

---

**Disclaimer**: This SDK is for informational purposes only and should not be considered as financial advice. Always do your own research and consult with financial professionals before making investment decisions.
```
