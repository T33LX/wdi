from progress.bar import Bar
from time import sleep
bar = Bar('Loading', fill='#', suffix='%(percent)d%%')
for i in range(100):
    sleep(0.01)
    bar.next()
bar.finish()

