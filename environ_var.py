import os

for var in ('HOME', 'USERPROFILE', 'HOMEPATH', 'HOMEDRIVE', 'JAVA_HOME'):
    print(os.environ.get(var))

print(os.environ['USERPROFILE'])
