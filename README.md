
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

![Guido van Rossum](pics/Guido_van_Rossum.png)

![Victor Stinner](pics/Victor_Stinner.png)

![Benjamin Peterson](pics/Benjamin_Peterson.png)

![Georg Brandl](pics/Georg_Brandl.png)

![Fred Drake](pics/Fred_Drake.png)

![Raymond Hettinger](pics/Raymond_Hettinger.png)

![Serhiy Storchaka](pics/Serhiy_Storchaka.png)

![Antoine Pitrou](pics/Antoine_Pitrou.png)

![Jack Jansen](pics/Jack_Jansen.png)

![Martin v. L�wis](pics/Martin_v._L�wis.png)

![Tim Peters](pics/Tim_Peters.png)

![Brett Cannon](pics/Brett_Cannon.png)

![Barry Warsaw](pics/Barry_Warsaw.png)

![Andrew M. Kuchling](pics/Andrew_M._Kuchling.png)

![Ezio Melotti](pics/Ezio_Melotti.png)

![Mark Dickinson](pics/Mark_Dickinson.png)

![Neal Norwitz](pics/Neal_Norwitz.png)

![Christian Heimes](pics/Christian_Heimes.png)

![R David Murray](pics/R_David_Murray.png)

![Senthil Kumaran](pics/Senthil_Kumaran.png)

![Gregory P. Smith](pics/Gregory_P._Smith.png)

![Terry Jan Reedy](pics/Terry_Jan_Reedy.png)

![Vinay Sajip](pics/Vinay_Sajip.png)

![�ric Araujo](pics/�ric_Araujo.png)

![Jeremy Hylton](pics/Jeremy_Hylton.png)

![Yury Selivanov](pics/Yury_Selivanov.png)

![Berker Peksag](pics/Berker_Peksag.png)

![Ned Deily](pics/Ned_Deily.png)

![Greg Ward](pics/Greg_Ward.png)

![Tarek Ziad�](pics/Tarek_Ziad�.png)

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
       2765: Martin v. L�wis
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
