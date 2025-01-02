from urllib.parse import urlparse, parse_qs

def extract_url_components(url):
    parsed_url = urlparse(url)
    protocol = parsed_url.scheme
    hostname = parsed_url.hostname
    domain_name = hostname if hostname else ""
    path = parsed_url.path
    directory, filename = path.rsplit("/", 1) if "/" in path else ("", path)

    query_parameters = parse_qs(parsed_url.query)

    return {
        "protocol": protocol,
        "hostname": hostname,
        "domain_name": domain_name,
        "directory": directory,
        "filename": filename,
        "query_parameters": query_parameters,
    }


if __name__ == "__main__":
    url= str(input("Enter URL:"))

    # Extract components
    components = extract_url_components(url)

    # Print results
    print(f"URL: {url}")
    print("Components:")
    print(f"  Protocol: {components['protocol']}")
    print(f"  Hostname: {components['hostname']}")
    print(f"  Domain Name: {components['domain_name']}")
    print(f"  Directory: {components['directory']}")
    print(f"  Filename: {components['filename']}")
    print(f"  Query Parameters: {components['query_parameters']}")
