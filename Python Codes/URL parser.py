from urllib.parse import urlparse

def url_splitter(url):
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract the parts
    protocol = parsed_url.scheme if parsed_url.scheme else "Does not Exist"
    host = parsed_url.hostname if parsed_url.hostname else "Does not Exist"
    port = parsed_url.port if parsed_url.port else "Does not Exist"
    path = parsed_url.path if parsed_url.path else "Does not Exist"
    
    # Print the extracted parts
    print(f"Protocol: {protocol}")
    print(f"Host/Domain: {host}")
    print(f"Port: {port}")
    print(f"Path: {path}")

# Test the function with the provided URL
url = "https://suno.com"
url_splitter(url)
