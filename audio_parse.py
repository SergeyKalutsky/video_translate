import os
import shutil
from tqdm import tqdm
from datetime import datetime
from pydub import AudioSegment
from text import parse_subtitles

shutil.rmtree('original')
os.mkdir('original')

texts, times = parse_subtitles('text.txt')

def time_diff(time1, time2):
    t1 = datetime.strptime(time1, '%M:%S')
    t2 = datetime.strptime(time2, '%M:%S')
    ts1 = (t1.minute*60 + t1.second) * 1000
    ts2 = (t2.minute*60 + t2.second) * 1000
    return ts1, ts2


song = AudioSegment.from_mp3("music.mp3")
for i in tqdm(range(len(times)-1)):
    ts1, ts2 = time_diff(times[i], times[i+1])
    segment = song[ts1:ts2]
    segment.export(f'original/{i}.mp3', format='mp3')
