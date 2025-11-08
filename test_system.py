"""
Quick test script to verify system components
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def test_imports():
    """Test that all imports work."""
    print("Testing imports...")
    try:
        from agents.retriever import ContextualRetrieverAgent
        from agents.analyzer import CriticalAnalysisAgent
        from agents.insight_generator import InsightGenerationAgent
        from agents.report_builder import ReportBuilderAgent
        from orchestration.coordinator import ResearchWorkflow
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_agents():
    """Test agent initialization."""
    print("\nTesting agent initialization...")
    try:
        from agents.retriever import ContextualRetrieverAgent
        from agents.analyzer import CriticalAnalysisAgent
        from agents.insight_generator import InsightGenerationAgent
        from agents.report_builder import ReportBuilderAgent
        
        retriever = ContextualRetrieverAgent()
        analyzer = CriticalAnalysisAgent()
        insight_gen = InsightGenerationAgent()
        report_builder = ReportBuilderAgent()
        
        print("✅ All agents initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Agent initialization error: {e}")
        return False

def test_workflow():
    """Test workflow initialization."""
    print("\nTesting workflow initialization...")
    try:
        from orchestration.coordinator import ResearchWorkflow
        
        workflow = ResearchWorkflow()
        print("✅ Workflow initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Workflow initialization error: {e}")
        return False

def test_api_key():
    """Check API key configuration."""
    print("\nChecking API key...")
    api_key = os.getenv("OPEN_ROUTER_KEY")
    if api_key and api_key != "your_openrouter_key_here":
        print("✅ OpenRouter API key configured")
        print(f"   Using OpenRouter endpoint: https://openrouter.ai/api/v1")
        return True
    else:
        print("⚠️  OpenRouter API key not configured (will use mock responses)")
        print("   Get your key from: https://openrouter.ai/keys")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing Multi-Agent AI Deep Researcher System\n")
    print("=" * 50)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Agents", test_agents()))
    results.append(("Workflow", test_workflow()))
    results.append(("API Key", test_api_key()))
    
    print("\n" + "=" * 50)
    print("\nTest Results:")
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {name}: {status}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n✅ All tests passed! System is ready.")
    else:
        print("\n⚠️  Some tests failed. Check errors above.")
    
    print("\nNext step: Run 'streamlit run app.py' to start the application")

if __name__ == "__main__":
    main()

