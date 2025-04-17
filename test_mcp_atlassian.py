from fastmcp import FastMCP, Client
from fastmcp.client.transports import FastMCPTransport, PythonStdioTransport, SSETransport
from dotenv import load_dotenv
from mcp_atlassian.confluence import ConfluenceFetcher, ConfluenceConfig

import json
import os
import asyncio

# Configure the ConfluenceFetcher
config = ConfluenceConfig(
    url=os.getenv("CONFLUENCE_URL"),
    auth_type="basic",
    username=os.getenv("CONFLUENCE_USERNAME"),
    ssl_verify=False,
    api_token=os.getenv("CONFLUENCE_TOKEN"),
    personal_token=os.getenv("CONFLUENCE_TOKEN")
)
# Initialize the ConfluenceFetcher
fetcher = ConfluenceFetcher(config=config)

# List spaces
def list_spaces():
    """
    List all spaces in the Confluence instance.
    """
    spaces = fetcher.get_spaces()
    print("Spaces:")
    for space in spaces['results']:
        print(f"- {space} \n")
        print(f"- {space['name']} (Key: {space['key']})")
    return spaces

#def search_pages(query: str):
#    """
#    Search for pages in Confluence.
#    """
#    pages = fetcher.search_pages(query=query)
#    print("Search Results:")
#    for page in pages:
#        print(f"- {page['title']} (ID: {page['id']})")
#    return pages

#def get_page(page_id: str):
#    """
#    Get a specific page by ID.
#    """
#    page = fetcher.get_page(page_id=page_id)
#    print(f"Page Title: {page['title']}")
#    print(f"Page Content: {page['body']['storage']['value']}")
#    return page


# Example usage
if __name__ == "__main__":
    import asyncio

    async def main():
        # List spaces
        spaces = list_spaces()
        
        # Search for pages
        #query = "MCP"
        #pages = await search_pages(query=query)
        
        # Get a specific page by ID
        #if pages:
        #    page_id = pages[0]['id']
        #    page = await get_page(page_id=page_id)

    asyncio.run(main())