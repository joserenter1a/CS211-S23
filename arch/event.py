import time

class Event:
    def __init__(self, name):
        self.name = name
        # Callback function
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def execute(self):
        print(f"Executing {self.name}...")
        time.sleep(1)
        print(f"{self.name} completed.")
        if self.callback:
            self.callback()

def start_routine():
    # Create events
    wake_up_event = Event("Wake up")
    get_dressed_event = Event("Get dressed")
    brush_teeth_event = Event("Brush teeth")
    ready_event = Event("Ready")
    # Set callbacks
    wake_up_event.set_callback(get_dressed_event.execute)
    get_dressed_event.set_callback(brush_teeth_event.execute)
    brush_teeth_event.set_callback(ready_event.execute)

    # Start morning routine
    wake_up_event.execute()



if __name__ == "__main__":
    start_routine()
