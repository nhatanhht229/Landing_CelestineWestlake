with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(1875, 1895):
    print(f'{i}: {lines[i].strip()}')
