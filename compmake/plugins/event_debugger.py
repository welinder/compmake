'''This plugin dumps all events received'''
import sys, time
from compmake.events.registrar import register_handler

# We save it, because it will be redirected during job execution
stream = sys.stderr
other_stream = sys.stdout

def print_event(event):
    other_stream.flush()
    
    age = time.time() - event.timestamp
    stream.write('%.3fs ago: %s: %s\n' % (age, event.name, event.kwargs))
    stream.flush()

register_handler("*", print_event)
