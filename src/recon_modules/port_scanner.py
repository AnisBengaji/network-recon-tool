import nmap
from datetime import datetime

def scan(target, port_range='1-1000'):
    nm = nmap.PortScanner()
    results = {
        'scan_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'open_ports': [],
        'host_status': 'unknown'
    }
    
    try:
        print(f"    Scanning {port_range}...")
        print(f"    Target: {target}")
        
        
        nm.scan(target, port_range, arguments='-Pn -sV -T4')
        
        
        print(f"    All hosts found: {nm.all_hosts()}")
        
        if nm.all_hosts():
            actual_target = nm.all_hosts()[0]
            print(f"    Scanning host: {actual_target}")
            
            results['host_status'] = nm[actual_target].state()
            print(f"    Host status: {results['host_status']}")
            
            if nm[actual_target].all_protocols():
                for proto in nm[actual_target].all_protocols():
                    print(f"    Protocol: {proto}")
                    ports = nm[actual_target][proto].keys()
                    print(f"    Ports to check: {list(ports)}")
                    
                    for port in ports:
                        info = nm[actual_target][proto][port]
                        print(f"    Port {port}: {info['state']}")
                        if info['state'] == 'open':
                            results['open_ports'].append({
                                'port': port,
                                'service': info.get('name', 'unknown'),
                                'version': info.get('version', '')
                            })
            else:
                print("    No protocols found!")
        else:
            print("    No hosts found!")
        
        print(f"    Found {len(results['open_ports'])} open ports")
    
    except Exception as e:
        results['error'] = str(e)
        print(f"    ERROR: {e}")
        import traceback
        traceback.print_exc()
    
    return results
