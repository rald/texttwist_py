import time
from threading import Timer


class SetInterval:

  def __init__(self, interval, func):
    self.interval = interval
    self.func = func
    self.timer = None
    self.is_running = False
    self.start()

  def _run(self):
    # Run the user function
    self.func()
    # Reschedule the next run if still active
    if self.is_running:
      self.start()

  def start(self):
    if not self.is_running:
      self.is_running = True
    # Create and start a new Timer
    self.timer = Timer(self.interval, self._run)
    self.timer.daemon = True
    self.timer.start()

  def stop(self):
    self.is_running = False
    if self.timer:
      self.timer.cancel()  # Cancels the pending timer


# --- How to use it ---
def my_task():
  print("Task executed!")


print("Starting interval...")
# Start running every 1 second
interval_task = SetInterval(1.0, my_task)

# Let it run for 3 seconds
time.sleep(3)

print("Stopping interval...")
interval_task.stop()

# Wait another 3 seconds to prove it has stopped (no more prints should appear)
time.sleep(3)
print("Program finished.")

