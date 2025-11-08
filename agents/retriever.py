"""
Contextual Retriever Agent
Pulls data from research papers, news articles, reports, and APIs.
"""

import logging
from typing import Dict, List, Any
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import ArxivAPIWrapper
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class ContextualRetrieverAgent:
    """Retrieves information from multiple sources: web, papers, and news."""
    
    def __init__(self):
        """Initialize retrieval tools."""
        try:
            self.web_search = DuckDuckGoSearchRun()
        except Exception as e:
            logger.warning(f"DuckDuckGo search not available: {e}")
            self.web_search = None
        
        try:
            self.arxiv = ArxivAPIWrapper()
        except Exception as e:
            logger.warning(f"Arxiv wrapper not available: {e}")
            self.arxiv = None
    
    def retrieve(self, query: str, max_results: int = 5) -> Dict[str, Any]:
        """
        Retrieve information from multiple sources.
        
        Args:
            query: Research query
            max_results: Maximum results per source type
            
        Returns:
            Dictionary with sources from web, papers, and news
        """
        logger.info(f"Retriever: Searching for '{query}'")
        
        results = {
            "web": [],
            "papers": [],
            "news": [],
            "query": query
        }
        
        # Web search
        if self.web_search:
            try:
                web_query = f"{query} recent"
                web_results = self.web_search.run(web_query)
                # Parse results (DuckDuckGo returns string, need to parse)
                results["web"] = self._parse_web_results(web_results, max_results)
                logger.info(f"Retriever: Found {len(results['web'])} web sources")
            except Exception as e:
                logger.error(f"Web search failed: {e}")
                results["web"] = []
        
        # ArXiv papers
        if self.arxiv:
            try:
                paper_results = self.arxiv.run(query)
                results["papers"] = self._parse_arxiv_results(paper_results, max_results)
                logger.info(f"Retriever: Found {len(results['papers'])} papers")
            except Exception as e:
                logger.error(f"ArXiv search failed: {e}")
                results["papers"] = []
        
        # News search (using web search with news filter)
        if self.web_search:
            try:
                news_query = f"{query} news 2024"
                news_results = self.web_search.run(news_query)
                results["news"] = self._parse_web_results(news_results, max_results)
                logger.info(f"Retriever: Found {len(results['news'])} news sources")
            except Exception as e:
                logger.error(f"News search failed: {e}")
                results["news"] = []
        
        return results
    
    def _parse_web_results(self, results: str, max_results: int) -> List[Dict[str, str]]:
        """Parse web search results into structured format."""
        parsed = []
        if not results:
            return parsed
        
        # DuckDuckGo returns a string, split by lines
        lines = results.split('\n')[:max_results * 2]  # Get more lines to parse
        
        current_entry = {}
        for line in lines:
            line = line.strip()
            if not line:
                if current_entry:
                    parsed.append(current_entry)
                    current_entry = {}
                continue
            
            # Try to extract title and snippet
            if 'http' in line or 'www.' in line:
                current_entry['url'] = line
            elif not current_entry.get('title'):
                current_entry['title'] = line
            else:
                current_entry['snippet'] = line
            
            if len(parsed) >= max_results:
                break
        
        if current_entry and len(parsed) < max_results:
            parsed.append(current_entry)
        
        return parsed
    
    def _parse_arxiv_results(self, results: str, max_results: int) -> List[Dict[str, str]]:
        """Parse ArXiv results into structured format."""
        parsed = []
        if not results:
            return parsed
        
        # ArXiv wrapper returns formatted string
        entries = results.split('\n\n')[:max_results]
        
        for entry in entries:
            lines = entry.split('\n')
            paper_entry = {
                'title': '',
                'authors': '',
                'summary': '',
                'url': ''
            }
            
            for line in lines:
                if 'Title:' in line:
                    paper_entry['title'] = line.replace('Title:', '').strip()
                elif 'Authors:' in line:
                    paper_entry['authors'] = line.replace('Authors:', '').strip()
                elif 'Summary:' in line:
                    paper_entry['summary'] = line.replace('Summary:', '').strip()
                elif 'arxiv.org' in line:
                    paper_entry['url'] = line.strip()
            
            if paper_entry['title']:
                parsed.append(paper_entry)
        
        return parsed

