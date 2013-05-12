import simplegui

# define global variables
time = 0
attempts = 0
success = 0
started = 0


# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = int(t/600)
    seconds = int((t%600)/10)
    milliseconds = t%10 
    if seconds < 10:
        formatted = str(minutes) + ":0" + str(seconds) + "." + str(milliseconds)
    else:
        formatted = str(minutes) + ":" + str(seconds) + "." + str(milliseconds)
    return formatted
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global started
    started=1
    timer.start()
    
def stop():
    global attempts
    global success
    global started
    if started==1:
        if time%10==0:
            success=success+1
            sound.play()
        started=0
        attempts=attempts+1
    timer.stop()
    
def reset():
    global time
    global attempts
    global success
    time = 0
    attempts=0
    success=0
    timer.stop()


# define event handler for timer with 0.1 sec interval

def tick():
    global time
    time = time + 1
        
def draw(canvas):
    canvas.draw_text(format(time), [100,100], 36, "White")
    canvas.draw_text(str(success)+"/"+str(attempts), [275,50], 14, "Green")
    
# create frame
frame = simplegui.create_frame("StopWatch", 300,200)
# lagniappe - added sound
sound = simplegui.load_sound("https://dl-web.dropbox.com/get/Public/ding.wav?w=AABBCdYCqAnKcyluYUs6ndE3MsEMdAWQVdvDfgaeICVdAA")
# register event handlers
timer = simplegui.create_timer(100, tick)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start timer and frame
frame.start()