#!/usr/bin/env python

#Code to monitor events
import sys
sys.path.append('usr/lib/python2.7/dist-packages/gtk-2.0')
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import pyinotify
import logging
from subprocess import call

#Setting up the log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ServerSync')
handler = logging.FileHandler('/home/jose/Desktop/TestingArea/ServerSync.log')

#Formats the log input
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Instance of a new WatchManager
wm = pyinotify.WatchManager()
mask = pyinotify.IN_MODIFY | pyinotify.IN_CREATE  # events to monitor


# Class to handle the events with certain actions depending on the event type
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(selfserlf, event):
        call(["rsync -zvh /home/jose/Desktop/TestingArea/TestMe.odt /home/jose/Desktop/", '-1'], shell=True)
        logger.info(':: File was synced %s', event.name)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/home/jose/Desktop/TestingArea/TestMe.odt', mask)

# Loop 4 lyfe
notifier.loop()