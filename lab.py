from gitcreeps import *
names = top_committers('data/cpython_log.txt', 30, return_names=True)
w = open('names.txt', 'w+')
for name in names:
    w.write(
'''
{0}
![{0}](pics/{1}.png)
'''.format(name, name.replace(' ', '_'))
    )
w.flush()
w.close()