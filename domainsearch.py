import argparse
import whois
import dns.resolver
import ssl
import socket
import requests
from bs4 import BeautifulSoup

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def print_section(title, data):
    print(YELLOW + f"{title}:" + RESET)
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{CYAN}{key}{RESET}: {value}")
    else:
        print(data)

def domain_search(domain):
    # Perform a WHOIS lookup
    w = whois.whois(domain)
    print_section("WHOIS Data", w)

    # Perform a DNS lookup
    dns_results = {}
    try:
        answers = dns.resolver.resolve(domain, 'A')
        dns_results['A'] = [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        pass

    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        dns_results['AAAA'] = [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        pass

    try:
        answers = dns.resolver.resolve(domain, 'MX')
        dns_results['MX'] = [str(rdata.exchange) for rdata in answers]
    except dns.resolver.NoAnswer:
        pass

    print_section("DNS Records", dns_results)

    # Check SSL certificate information
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()
        print_section("SSL Certificate Information", cert)
    except Exception as e:
        print(RED + "SSL Certificate Information not available:", e + RESET)

    # Search for mentions of the domain on various websites
    print(YELLOW + "Mentions on Websites:" + RESET)
    search_url = f"https://www.google.com/search?q={domain}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('a')
            for link in results:
                print(link.get('href'))
    except requests.RequestException as e:
        print(RED + "Error fetching mentions:", e + RESET)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Domain Search Module - BlackSearch")
    parser.add_argument("-d", "--domain", help="The domain name to search for")
    args = parser.parse_args()

    if args.domain:
        domain_search(args.domain)
    else:
        print(RED + "Please provide a domain name using -d or --domain option." + RESET)
