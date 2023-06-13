def parse_subtitles(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()

    lines = [line.replace('\n', '') for line in data[1::2]]
    times = [line.replace('\n', '') for line in data[0::2]]
    return lines, times


