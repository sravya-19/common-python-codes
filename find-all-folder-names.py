import os

path = ''
print([name for name in os.listdir(path) if os.path.isdir(name)])
