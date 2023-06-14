def parse_subtitles(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()

    lines = [line.replace('\n', '') for line in data[1::2]]
    times = [line.replace('\n', '') for line in data[0::2]]
    return lines, times


def reasamble_text(fname, n_lines):
    lines, times = parse_subtitles(fname)
    new_lines = ''
    for i in range(len(lines)//n_lines + 1):
        new_lines += times[i*n_lines] + '\n' + \
            ' '.join(lines[i*n_lines: (i+1)*n_lines]) + '\n'
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write(new_lines)
