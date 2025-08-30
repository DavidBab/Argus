import requests
from concurrent.futures import ThreadPoolExecutor

def subdomain_search(domain, wordlist, max_threads=50, output=None):
    file_handle = None
    if output:
        file_handle = open(output, "w")

    with open(wordlist, "r") as f, ThreadPoolExecutor(max_workers=max_threads) as executor:
        for subdomain in f:
            subdomain = subdomain.strip()
            executor.submit(check_subdomain, domain, subdomain, file_handle)
    
    if file_handle:
        file_handle.close()


def check_subdomain(domain, subdomain, file_handle):
    req = f"{subdomain}.{domain}"

    try:
        requests.get(f"http://{req}")
    except requests.ConnectionError:
        pass
    else:
        line = f"[+] {req}"

        if file_handle:
            file_handle.write(line + "\n")
        else:
            print(f"\033[92m{line}\033[0m")

    

