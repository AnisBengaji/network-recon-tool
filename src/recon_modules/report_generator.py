import json
from jinja2 import Template
from datetime import datetime
import os

def generate(results, output_name):
    os.makedirs('reports', exist_ok=True)
    
    # Save JSON
    json_file = f'reports/{output_name}.json'
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=4)
    
    # Save HTML
    html_file = f'reports/{output_name}.html'
    html = create_html(results)
    with open(html_file, 'w') as f:
        f.write(html)

def create_html(results):
    template = Template('''
<!DOCTYPE html>
<html>
<head>
    <title>Recon Report - {{ results.target }}</title>
    <style>
        body { font-family: Arial; max-width: 1000px; margin: 50px auto; background: #f5f5f5; }
        .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        .section { margin: 30px 0; padding: 20px; background: #ecf0f1; border-radius: 5px; }
        h2 { color: #3498db; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #bdc3c7; }
        th { background: #3498db; color: white; }
        .open { background: #2ecc71; color: white; padding: 5px 10px; border-radius: 3px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Reconnaissance Report</h1>
        <p><strong>Target:</strong> {{ results.target }}</p>
        <p><strong>Date:</strong> {{ now }}</p>
        
        {% if results.ports %}
        <div class="section">
            <h2>📡 Open Ports</h2>
            <p>Status: {{ results.ports.host_status }}</p>
            <table>
                <tr><th>Port</th><th>Service</th><th>Version</th><th>Status</th></tr>
                {% for port in results.ports.open_ports %}
                <tr>
                    <td>{{ port.port }}</td>
                    <td>{{ port.service }}</td>
                    <td>{{ port.version }}</td>
                    <td><span class="open">OPEN</span></td>
                </tr>
                {% endfor %}
            </table>
        </div>
        {% endif %}
        
        {% if results.dns %}
        <div class="section">
            <h2>🌐 DNS Records</h2>
            {% for type, records in results.dns.records.items() %}
            <p><strong>{{ type }}:</strong> {{ records|join(', ') }}</p>
            {% endfor %}
        </div>
        {% endif %}
        
        {% if results.whois %}
        <div class="section">
            <h2>📋 WHOIS Info</h2>
            <p><strong>Registrar:</strong> {{ results.whois.info.registrar }}</p>
            <p><strong>Created:</strong> {{ results.whois.info.created }}</p>
            <p><strong>Expires:</strong> {{ results.whois.info.expires }}</p>
        </div>
        {% endif %}
        
        <div style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #ecf0f1; text-align: center; color: #7f8c8d;">
            <p>⚠️ For authorized testing only</p>
            <p>Created by Anis Bengaji</p>
        </div>
    </div>
</body>
</html>
    ''')
    
    return template.render(results=results, now=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
