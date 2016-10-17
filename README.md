# ServerSync.py

A 2.7 Python script that uses Rsync to copy a config file from one server to another while maintaining a log file of the syncs.

Currently set to work using Upstart so that it can be a service that starts at boot and can be started and stopped via the command Sudo start ServerSync. 

ServerSync.config also attached here. Make sure to place this in /etc/init/
