#import datetime
#Oras = "The Local Time and Date Now Is"
#KarungOrasa =datetime.datetime.now() .isoformat()
#print (Oras, KarungOrasa)
# Display Local Machine Date and Time in 24 or Mil format
#import datetime
#current_time = datetime.datetime.now()
#time_string = current_time.strftime("The local time and date now is %I:%M %p on %B %d, %Y")
#import datetime
#print(time_string)

import datetime
current_time = datetime.datetime.now()
time_string = current_time.strftime("The local time and date now is %H:%M on %B %d, %Y")
print(time_string)
import tkinter as tk
import datetime

# Create the main window
root = tk.Tk()
root.title("Clock")

# Create a label to display the current time
label = tk.Label(root, font=("Roboto", 40))
label.pack()

# Update the time every 1000 milliseconds (1 second)
def update_time():
    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%I:%M:%S %p")
    label.configure(text=time_string)
    root.after(1000, update_time)

# Run the update_time function for the first time
update_time()

# Run the Tkinter event loop
root.mainloop()
