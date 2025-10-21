import dns.resolver
from datetime import datetime

def enumerate(target):
    results = {
        'scan_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'records': {}
    }
    
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    
    for rec_type in record_types:
        try:
            answers = dns.resolver.resolve(target, rec_type)
            results['records'][rec_type] = [str(r) for r in answers]
            print(f"    Found {len(results['records'][rec_type])} {rec_type} records")
        except:
            results['records'][rec_type] = ['None found']
    
    return results
