import requests
from concurrent.futures import ThreadPoolExecutor

valid_codes = [
    200,  # OK
    201,  # Created
    202,  # Accepted
    203,  # Non-Authoritative Information
    204,  # No Content
    206,  # Partial Content
    301,  # Moved Permanently
    302,  # Found (redirect)
    303,  # See Other
    304,  # Not Modified
    307,  # Temporary Redirect
    308,  # Permanent Redirect
    401,  # Unauthorized (may exist, but needs auth)
    403,  # Forbidden (exists, but access denied)
    405,  # Method Not Allowed (may exist, but wrong method)
]


def dir_search(domain, wordlist, max_threads=50, output=None):
    file_handle = None
    if output:
        file_handle = open(output, "w")

    with open(wordlist, "r") as f, ThreadPoolExecutor(max_workers=max_threads) as executor:
        for directory in f:
            directory = directory.strip()
            executor.submit(check_directory, domain, directory, file_handle)

    if file_handle:
        file_handle.close()


def check_directory(domain, directory, file_handle):
    req = f"{domain}/{directory}"

    try:
        response = requests.get(f"http://{req}")

    except requests.ConnectionError:
        pass

    else:
        line = ""
        if response.status_code in valid_codes:
            line = f"[{response.status_code}] {directory}"
        
        if file_handle and line:
            file_handle.write(line + "\n")
        elif line:
            print(f"\033[92m{line}\033[0m")
