#!/usr/bin/env python3

import argparse
import modules.dns_resolve as dnsres
import modules.subdom_enum as domenum
import modules.dir_enum as direnum


def main():
    # Argument Parsing
    parser = argparse.ArgumentParser(description="Argus CLI tool")
    parser.add_argument("-r", "--record", metavar="", default=None, help="Specify the DNS record type to query (e.g., A, MX, TXT, all). If omitted, scans common types.")
    parser.add_argument("-s", "--sub-enum", default=None, metavar="", help="Enumerate subdomains using a wordlist")
    parser.add_argument("-d", "--dir-enum", default=None, metavar="", help="Enumerate directories using a wordlist")
    parser.add_argument("-w", "--wordlist", default=None, metavar="", help="Specify wordlist to use (required for specific tasks)")
    parser.add_argument("domain", nargs="?", default="shelltutor.com", help="Domain to query")
    args = parser.parse_args()

    # DNS Record Resolve
    if args.record:
        dnsres.dns_records(args.domain, args.record)

    if args.sub_enum:
        pass


if __name__ == "__main__":
    main()




