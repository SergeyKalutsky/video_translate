from tqdm import tqdm
from pydub import AudioSegment

combined = AudioSegment.silent(duration=1000)
for i in tqdm(range(351)):
    try:
        sound2 = AudioSegment.from_mp3(f"original/{i}.mp3")
        sound1 = AudioSegment.from_mp3(f"translated/{i}.mp3")
        combined += sound1 + AudioSegment.silent(duration=1000) + sound2
        combined += AudioSegment.silent(duration=1000) + sound2
    except:
        continue

file_handle = combined.export("ĐCNNTK #25.mp3", format="mp3")
