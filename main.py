from tqdm import tqdm
from glob import glob
import os

sum = 0
for i in tqdm(range(100), desc="loop 1 "):
	sum += i

print('sum -- ', sum)
pretext = os.environ.get('PRETEXT', "")

# print(glob('./*'))

with open('/data/new_file.txt', 'a') as f:
    f.write(pretext + " : " + str(sum) + '\n')

