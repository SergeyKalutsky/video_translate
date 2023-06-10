with open('text.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

lines = [line.replace('\n', '') for line in data if not line[0].isdigit()]
print(len(lines))
time = [line.replace('\n', '') for line in data if line[0].isdigit()]
lines = '\n'.join(lines)

with open('plain.txt', 'w', encoding='utf-8') as f:
    f.write(lines)
