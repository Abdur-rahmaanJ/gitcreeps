from gitcreeps import *

w = open('README.md', 'w+')

w.write(
'''
# gitcreeps

The library for sneaking on committers! 

For example we see Barry Warsaw committing around 03am on sunday 
you'll be sure that he has a high probability
of being at his PC on that day.

We see that Mr. Guido has his free time everyday around 07am (He has the 
least probability of being at his PC everyday at 07am, that leaves
room for the possibility that he's surfing the internet at that time. 
Free times are poor clues by themselves.)

Mr. Jack Jansen seems to return home around 6pm, maybe he's on his transport around
that time. He's also seen leaving much uncommitted times in the morning, which 
suggests that maybe he's preparing to leave home and take his transport. He maybe 
uses public transport.

The most probable time you'll see Brett Cannon at his PC is on a Friday at 4pm.

Psst. those are just assumptions!

Here are the patterns for the top 30 committers of cpython:
'''
    )

# pics
names = top_committers('data/cpython_log.txt', 30, return_names=True)
for name in names:
    w.write(
'''
![{0}](pics/{1}.png)
'''.format(name, name.replace(' ', '_'))
    )

w.write(
'''
# Docs

### def to_json_file(data, filename):

converts dictionary to .json file

### def parse_log(file_name):

returns generated data (by the command 

git shortlog --format=format:%cI > log.txt)

in the repository. returns dict:
```
{
    "4kir4": [
        "2017-03-20T08:44:46+02:00"
    ],
    "A. Jesse Jiryu Davis": [
        "2018-06-04T19:57:08+09:00"
    ],
    "AMIR": [
        "2019-10-22T21:05:54-03:00"
    ], ...
```

### def get_clean_data(logfilename):

    produces data in the format:
```
    "Abdur-Rahmaan Janhangeer": {
        "monday": {
            "commits": 19,
            "times": [
                "2019-03-11@06:42:39",
                "2019-03-25@02:59:00"
            ]
        },
        "tuesday": {
        ...
    }
```

### def merge_names(clean_data, namelist, default=None):

namelist is a list of names to be grouped under a default name.
one thing is that people sometimes commit under different names.
modifies clean data

### def plot_user(data, name, alpha=0.1):

plots chart for single user where data is clean_data

### def save_user_plot(data, name, alpha=0.01):

save chart for single user where data is clean_data

### def save_users_plot(data, names, alpha=0.1):

save chart for multiple users

### def top_committers(filepath, number, return_=False, return_names=False):

no return prints out

```
Top 20 committers for data/cpython_log.txt:
      11192: Guido van Rossum
       5919: Victor Stinner
       5829: Benjamin Peterson
       5677: Georg Brandl
       5465: Fred Drake
       4151: Raymond Hettinger
       3972: Serhiy Storchaka
       3765: Antoine Pitrou
       2978: Jack Jansen
       2765: Martin v. Löwis
       2517: Tim Peters
       2105: Brett Cannon
       2087: Barry Warsaw
       2032: Andrew M. Kuchling
       1999: Ezio Melotti
       1922: Mark Dickinson
       1815: Neal Norwitz
       1361: Christian Heimes
       1341: R David Murray
       1237: Senthil Kumaran
```

return_ returns the whole data [[name1, commits], [name2, commits]]

return_names returns [[name1, name2, name3]]
'''
    )

w.flush()
w.close()