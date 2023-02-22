import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/lee/Documents"
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"ola,{event.scr_path}foi criado!")
    
    def on_modifield(self, event):
        print(f"ola,{event.scr_path}foi modificado!")

    def on_moved(self, event):
        print(f"ola,{event.scr_path}foi movido ou renomeado!")

    def on_deleted(self, event):
        print(f"opa! alguem excluiu {event.scr_path}!")


event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()