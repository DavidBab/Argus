import requests
from concurrent.futures import ThreadPoolExecutor

valid_codes = [
    200,  # OK
    201,  # Created
    202,  # Accepted
    203,  # Non-Authoritative Information
    204,  # No Content
    206,  # Partial Content
]

redirect_codes = [
    301,  # Moved Permanently
    302,  # Found (redirect)
    303,  # See Other
    304,  # Not Modified
    307,  # Temporary Redirect
    308,  # Permanent Redirect
]

forbidden_codes = [
    401,  # Unauthorized (may exist, but needs auth)
    403,  # Forbidden (exists, but access denied)
    405,  # Method Not Allowed (may exist, but wrong method)
]

def dir_search(domain, wordlist, max_threads=50):

    with open(wordlist, "r") as f, ThreadPoolExecutor(max_workers=max_threads) as executor:
        for directory in f:
            directory = directory.strip()
            executor.submit(check_directory, domain, directory)


def check_directory(domain, directory):
    req = f"{domain}/{directory}"

    try:
        response = requests.get(f"http://{req}")
        if response.status_code in [404]:
            return
        
    except requests.ConnectionError:
        pass

    else:
        if response.status_code in valid_codes:
            print(f"\033[92m[{response.status_code}] {req}\033[0m")

        elif response.status_code in forbidden_codes:
            print(f"\033[91m[{response.status_code}] {req}\033[0m")

        elif response.status_code in redirect_codes:
            print(f"\033[93m[{response.status_code}] {req}\033[0m")
