# Changelog

## OpenRouter Integration Update

### Changes Made

1. **LLM Configuration**
   - Created `utils/llm_config.py` for centralized LLM configuration
   - Switched from direct OpenAI API to OpenRouter API
   - Supports multiple LLM providers through unified interface

2. **Agent Updates**
   - Updated `agents/analyzer.py` to use OpenRouter
   - Updated `agents/insight_generator.py` to use OpenRouter
   - Updated `agents/report_builder.py` to use OpenRouter
   - All agents now use `create_llm()` utility function

3. **Configuration Files**
   - Changed `.env.example` to `env.example` (OpenRouter format)
   - Updated API key from `OPENAI_API_KEY` to `OPEN_ROUTER_KEY`
   - Added model configuration in `utils/llm_config.py`

4. **Documentation**
   - Updated `README.md` with OpenRouter setup instructions
   - Updated `QUICK_START.md` with OpenRouter API key steps
   - Created `OPENROUTER_SETUP.md` with detailed setup guide
   - Updated `setup.py` to use OpenRouter
   - Updated `test_system.py` to check for OpenRouter key

### Benefits

- **Unified API**: Single API key for multiple LLM providers
- **Flexibility**: Easy to switch between models (OpenAI, Anthropic, Google, etc.)
- **Cost Effective**: OpenRouter often has better pricing
- **Reliability**: Multiple provider fallbacks
- **Access**: Some models available without waitlists

### Migration Guide

**Before:**
```bash
OPENAI_API_KEY=sk-your-key-here
```

**After:**
```bash
OPEN_ROUTER_KEY=sk-or-your-key-here
```

Get your key from: https://openrouter.ai/keys

### Model Format

**Before:**
```python
model = "gpt-4-turbo-preview"
```

**After:**
```python
model = "openai/gpt-4-turbo-preview"  # OpenRouter format
```

### Configuration

Edit `utils/llm_config.py` to change models:
- `DEFAULT_MODEL` - Default for all agents
- `ANALYZER_MODEL` - Analysis agent
- `INSIGHT_MODEL` - Insight generation
- `REPORT_MODEL` - Report building

---

**Updated**: System now uses OpenRouter for LLM access

