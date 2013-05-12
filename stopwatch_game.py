import simplegui

# define global variables
time = 0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(total_milliseconds):
    minutes = int(total_milliseconds/600)
    seconds = int((total_milliseconds%600)/10)
    milliseconds = total_milliseconds%10 
    if seconds < 10:
        formatted = str(minutes) + ":0" + str(seconds) + "." + str(milliseconds)
    else:
        formatted = str(minutes) + ":" + str(seconds) + "." + str(milliseconds)
    return formatted
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    global time
    time = 0.00
    timer.stop()


# define event handler for timer with 0.1 sec interval

def tick():
    global time
    time = time + 1
        
def draw(canvas):
    canvas.draw_text(format(time), [100,100], 36, "White")
    
    
# create frame
frame = simplegui.create_frame("StopWatch", 300,200)

# register event handlers
timer = simplegui.create_timer(100, tick)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start timer and frame
frame.start()