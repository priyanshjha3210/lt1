import base64
import re

with open('logo.png', 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')
    
b64_url = f"url(data:image/png;base64,{b64_data})"

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the circular reference in :root
html = re.sub(r'--logo-b64:\s*var\(--logo-b64\);', f'--logo-b64: {b64_url};', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
