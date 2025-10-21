import whois
from datetime import datetime

def lookup(target):
    results = {
        'scan_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'info': {}
    }
    
    try:
        w = whois.whois(target)
        
        results['info'] = {
            'domain': str(w.domain_name) if w.domain_name else 'N/A',
            'registrar': w.registrar or 'N/A',
            'created': str(w.creation_date) if w.creation_date else 'N/A',
            'expires': str(w.expiration_date) if w.expiration_date else 'N/A',
            'country': w.country or 'N/A'
        }
        
        print(f"    Registrar: {results['info']['registrar']}")
    
    except Exception as e:
        results['error'] = str(e)
        print(f"    Error: {e}")
    
    return results
