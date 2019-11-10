import maya

x = maya.parse('2019-11-10T11:04:35+04:00').datetime()
print(dir(x))
print(x.time())

def buzz(x):
	del x[1]

x = {1:2, 2:3}
buzz(x)

print(x)