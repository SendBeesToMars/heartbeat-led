import tkinter as tk

root = tk.Tk()
root.attributes('-alpha', 0.0) #For icon
#root.lower()
root.iconify()
window = tk.Toplevel(root)
window.geometry("34x34") #Whatever size
window.overrideredirect(True) #Remove border
window.attributes('-topmost', 1)
#Whatever buttons, etc 
bg = "#99ff22"
close = tk.Button(window, command = lambda: defibrillator(), bg=bg)
close.pack(fill = tk.BOTH, expand = 1)

count = 0 # hides window
count_2_electric_boogaloo = 0 #stop program flag
heart_rate = 500
heart_rate_rate = 0.05 # increase time between function calls
heart_rate_rate_rate = 1.0005 # increase time between function calls

def defibrillator():
    global count_2_electric_boogaloo
    if count_2_electric_boogaloo:
        print(count_2_electric_boogaloo)
        root.destroy()
    count_2_electric_boogaloo += 1
    heart()

def heart():
    global heart_rate, heart_rate_rate, heart_rate_rate_rate
    heart_rate_copy = heart_rate
    root.after(round(heart_rate_copy), electrocardiograph) # only accepts integers :)
    if heart_rate < 1000:
        heart_rate_rate = heart_rate_rate * heart_rate_rate_rate
        heart_rate += heart_rate_rate

def electrocardiograph():
    global count 
    if (count == 0 ):
        count += 1
        window.deiconify()
    else:
        count = 0
        window.withdraw()
    heart()

root.mainloop()
