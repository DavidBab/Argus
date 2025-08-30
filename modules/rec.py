import dns.resolver

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def dns_records(target_domain):
    record_types = ["A", "AAAA", "CNAME", "MX", "TXT", "SOA"]
    resolver = dns.resolver.Resolver()
   
    for rec_type in record_types:
        dns_check(domain=target_domain, record=rec_type, resolver=resolver)


def visualize(answer):
    for data in answer:
        print(f"{GREEN}[+]{RESET} {data}")


def dns_check(domain, record, resolver):
    try:
        answer = resolver.resolve(domain, record)
        print(f"{record} records for {domain}")
        visualize(answer=answer)

    except dns.resolver.NoAnswer:
        print(f"Sorry, couldn't find any record for {record}.")

    except Exception as e:
        print(f"{e}")
