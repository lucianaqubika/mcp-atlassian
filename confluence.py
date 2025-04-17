from atlassian import Confluence
import os
from dotenv import load_dotenv
load_dotenv()

confluence = Confluence(
    url=os.getenv("CONFLUENCE_URL"),
    username=os.getenv("CONFLUENCE_USERNAME"),
    password=os.getenv("CONFLUENCE_TOKEN"),
    cloud=True
)

### SPACES ###
def get_all_spaces():
    """
    List all spaces in the Confluence instance.
    """
    # Get all spaces with provided limit
    # additional info, e.g. metadata, icon, description, homepage
    spaces = confluence.get_all_spaces(start=0, limit=500, expand=None)
    #spaces = confluence.get_spaces()
    print("Spaces:")
    for space in spaces['results']:
        print(f"- {space}\n")
    return spaces

def get_space_by_key(space_key :str):
    """
    Get a specific space by its key.
    """
    space = confluence.get_space(space_key, expand='description.plain,homepage')
    print(f"Space Title: {space['name']}")
    print(f"Space Key: {space['key']}")
    return space

def get_space_content(space_key: str):
    """
    Get all content in a specific space.
    """
    # Get all content with provided limit
    # additional info, e.g. metadata, icon, description, homepage
    content = confluence.get_space_content(space_key, start=0, limit=500, expand="body.storage")
    print(f"Content in Space '{space_key}':")
    #print(f"Content :{content}")
    for item in content['page']['results']:
       
        print(f"- {item['title']} (ID: {item['id']})")
    return content

def get_space_permissions(space_key: str):
    """
    Get permissions for a specific space.
    """
    # Get all permissions with provided limit
    # additional info, e.g. metadata, icon, description, homepage
    permissions = confluence.get_space_permissions(space_key)
    print(f"Permissions for Space '{space_key}':")
    for item in permissions['results']:
        print(f"- {item['operation']} (ID: {item['id']})")
    return permissions
### SPACES ###

### PAGES ###
def is_page_exists(space: str, title: str):
    """
    Check if a page exists in a given space.
    """
    return confluence.page_exists(space, title)
    
def get_page_by_title(space: str, title: str):
    """
    Get a specific page by its title in a given space.
    """
    page = confluence.get_page_by_title(space, title,)
    print(f"Page: {page['title']} (ID: {page['content']['id']}) - URL: {page['url']}")
   
    return page

def get_page_by_id(page_id: str):
    """
    Get a specific page by its ID.
    """
    page = confluence.get_page_by_id(page_id)
    print(f"Page ID: {page_id}")
    print(f"Page: {page}")
    print(f"Page: {page['title']} (ID: {page['id']})")
    
    return page

def get_page_labels(page_id: str):
    """
    Get The list of labels on a piece of Content
    """
    labels = confluence.get_page_labels(page_id)
    print(f"Labels for Page '{page_id}':")
    for label in labels['results']:

        print(f"- {label}")
   
    return labels['results']

def get_all_pages_by_label(label: str):
    """
    Get all pages with a specific label.
    """
    pages = confluence.get_all_pages_by_label(label, start=0, limit=50, expand=None)
    print(f"Pages with Label '{label}':")
    for page in pages:
        print(f"- {page['title']} (ID: {page['content']['id']}) - URL: {page['url']}")
    return pages


def get_all_pages_from_space(space_key: str):
    """
    Get all pages from a specific space.
    """
    pages = confluence.get_all_pages_from_space(space_key, start=0, limit=100, status=None, expand=None, content_type='page')
    print(f"Pages in Space '{space_key}':")
    for page in pages:
        print(f"- {page['title']} (ID: {page['content']['id']}) - URL: {page['url']}")
    return pages

def create_page(space: str, title: str, body: str):
    """
    Create a new page in a given space.
    """
    page = confluence.create_page(space, title, body, parent_id=None, type='page', representation='storage', editor='v2', full_width=False)
    print(f"Page Created: {page['title']} (ID: {page['content']['id']}) - URL: {page['url']}")
    return page

def update_page(page_id: str, title: str, body: str):
    """
    Update an existing page by its ID.
    """
    page = confluence.update_page(page_id, title, body, parent_id=None, type='page', representation='storage', minor_edit=False, full_width=False)
    print(f"Page Updated: {page['title']} (ID: {page['content']['id']}) - URL: {page['url']}")
    return page

def update_or_create_page(parent_id: str, title: str, body: str):
    """
    Update page or create page if it is not exists
    """
    page = confluence.update_or_create_page(parent_id, title, body, representation='storage', full_width=False)
    print(f"Page Updated/Created: {page['title']} (ID: {page['content']['id']}) - URL: {page['url']}")
    return page

def append_page(page_id: str, title: str, append_body: str):
    """
    Append content to an existing page by its ID.
    """
    page = confluence.append_page(page_id, title, append_body, parent_id=None, type='page', representation='storage', minor_edit=False)
    print(f"Page Appended: {page['title']} (ID: {page['content']['id']}) - URL: {page['url']})")
    return page

def move_page(space_key: str, page_id: str, target_title: str):
    """
    Move a page to a new location within the same space.
    """
    page = confluence.move_page(space_key, page_id, target_title, position="append")
    print(f"Page Moved: {page['title']} (ID: {page['content']['id']}) - URL: {page['url']}")
    return page

### SEARCH ###
def search_pages(cql: str):
    """
    Search for pages in Confluence using CQL.
    """
    pages = confluence.cql(cql, start=0, limit=None, expand=None, include_archived_spaces=None, excerpt=None)
    print("Search Results:")
    for page in pages['results']:
        print(f"- {page['title']} (ID: {page['content']['id']}) - URL: {page['url']} : \n {page['excerpt']} \n")
    return pages

# Example usage
if __name__ == "__main__":
    import asyncio

    async def main():

        # TESTING
        print("--- Testing Confluence API")
        # List spaces
        spaces = get_all_spaces()
       
       # Search
        cql = 'type=page and title~"MCP"'
        pages = search_pages(cql=cql)
         
          # Get a specific page by ID
        if pages:
            page_id = pages['results'][0]['content']['id']
            print(f"Page ID: {page_id}")
            page = get_page_by_id(page_id=page_id)
            
            # Get labels for the page
            labels = get_page_labels(page_id=page_id)
            
            # Get all pages with a specific label
            label = labels[0] if labels else None
            if label:
                all_pages = get_all_pages_by_label(label=label)
          
        # Get space content
        space_key = spaces['results'][0]['key'] if spaces['results'] else None
        if space_key:
            content = get_space_content(space_key=space_key)
        
        print("----------")

    asyncio.run(main())