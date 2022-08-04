''' lib_vrlc.py

This file simulates being a module for use by Pyodide,
allowing Python-defined "library" files to be defined
and "built-in" as far as student Python programmers are
concerned.   However, it is not actually imported, but
in VRLC Alpha it is executed at the beginning of the
session, so that its methods will be available.
This is to get around Pyodide's complicated process
for having separate user-defined modules.

 Version 001b.   Jan. 20, 2022.  By SLT.
'''



import pyodide
from js import document   # access to the DOM, for registering event handlers.

def default_vrlc_event_handler(event):
  '''In case no alternative handler is defined and requested.
  This could be helpful in making sure handler is correctly registered.'''
  print("Detected event: "+event.type+", on current target: "+event.currentTarget)

class makeHandler:
  '''Used to create, register, store, unregister and destroy proxies for handlers.
  Proxies are required so that Javascript can call the Python functions.'''
  proxy_list = []

  def __init__(self, eventType, DOM_ElementId, function_to_call=default_vrlc_event_handler):
   # Create a proxy:
   self.proxy = pyodide.create_proxy(function_to_call)

   # Register the proxy on the DOM
   document.getElementById(DOM_ElementId).addEventListener(eventType, self.proxy)
   makeHandler.proxy_list.append((eventType, DOM_ElementId, self.proxy))
   
  # A Class method:
  def unregister_and_destroy_proxy( eventType, DOM_ElementId, proxy):
     document.getElementById(DOM_ElementId).removeEventListener(eventType, proxy)
     proxy.destroy()

  # A Class method:
  def destroy_all_proxies():
   for (eventType, DOM_ElementId, proxy) in makeHandler.proxy_list:
       unregister_and_destroy_proxy(eventType, DOM_ElementId, proxy)
   makeHandler.proxy_list = []   


# For testing, and as a reminder to incorporate the Tones.js package
# so at least some audio cues can be set up in handlers.
def when_body_double_clicked(event):
  print("\a") # Beep?

makeHandler("dblclick", "the_body", when_body_double_clicked)

