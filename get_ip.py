#Submitted by Himanshu Choudhary
import socket
from urllib.parse import urlparse

def get_ip_address(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.split(":")[0]  # Extract the domain without the port (if any)
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    website = input("Enter the website URL: ")
    ip = get_ip_address(website)
    if ip:
        print(f"The IP address of {website} is: {ip}")

