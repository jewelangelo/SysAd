import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)  # in bytes 
