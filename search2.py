with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'id=' in l and 'gioi-thieu' in l:
        print(f'{i}: {l.strip()[:100]}')
    if 'Vị trí hiếm hoi' in l:
        print(f'{i}: {l.strip()[:100]}')
