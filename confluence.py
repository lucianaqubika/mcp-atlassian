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
    for item in content['results']:
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
    print(f"Page Title: {page['title']}")
    print(f"Page ID: {page['id']}")
    return page

def 



# Example usage
if __name__ == "__main__":
    import asyncio

    async def main():
        # List spaces
        spaces = get_all_spaces()
       

    asyncio.run(main())