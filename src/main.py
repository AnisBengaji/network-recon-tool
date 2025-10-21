#!/usr/bin/env python3
import argparse
from colorama import Fore, Style, init
from recon_modules import port_scanner, dns_enum, whois_lookup, report_generator

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}═══════════════════════════════════════════
    Network Recon Tool v1.0
    By Anis Bengaji
═══════════════════════════════════════════{Style.RESET_ALL}
    """
    print(banner)

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Network Reconnaissance Tool")
    parser.add_argument('target', help='Target domain or IP (e.g., example.com)')
    parser.add_argument('-p', '--ports', default='1-1000', help='Port range')
    parser.add_argument('-o', '--output', default='report', help='Report name')
    
    args = parser.parse_args()
    
    print(f"{Fore.GREEN}[+] Target: {args.target}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Starting scan...{Style.RESET_ALL}\n")
    
    results = {'target': args.target}
    
    # Run each module
    print(f"{Fore.CYAN}[1/4] Scanning ports...{Style.RESET_ALL}")
    results['ports'] = port_scanner.scan(args.target, args.ports)
    
    print(f"{Fore.CYAN}[2/4] Checking DNS...{Style.RESET_ALL}")
    results['dns'] = dns_enum.enumerate(args.target)
    
    print(f"{Fore.CYAN}[3/4] Getting WHOIS info...{Style.RESET_ALL}")
    results['whois'] = whois_lookup.lookup(args.target)
    
    print(f"{Fore.CYAN}[4/4] Generating report...{Style.RESET_ALL}")
    report_generator.generate(results, args.output)
    
    print(f"\n{Fore.GREEN}✓ Done! Report saved: reports/{args.output}.html{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
