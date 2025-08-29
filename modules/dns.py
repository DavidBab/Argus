import requests
from concurrent.futures import ThreadPoolExecutor

def subdomain_search(domain, wordlist, max_threads=50):

    with open(wordlist, "r") as f, ThreadPoolExecutor(max_workers=max_threads) as executor:
        for subdomain in f:
            subdomain = subdomain.strip()
            executor.submit(check_subdomain, domain, subdomain)


def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"

    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(f"\033[92m[+] {url}\033[0m")

    

