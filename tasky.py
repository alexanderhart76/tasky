import webbrowser
import time


# figures out if timelength is an integer. if not, the function locks you into a loop until you correct it,
def isnumber(timelength):
    global isnumber #is this a good idea?

    while True: #forever loop
        try: # executes arguments in try block and jumps to except if an error occurs
            isnumber = int(timelength) #assigns integer status to user input. if input wasn't an int an error occurs which triggers except block.
            break
        except ValueError: #executes block if try reached a ValueError
            print "Please enter a number you retard." #fucking niggers
            timelength = raw_input()


#takes input from "How long would you like to work on this task?" and sleeps the program for x minutes. performs time measurements to prove that function is working correctly.
def apptime(isnumber):
    print 'Started timer.'
    start = time.time() # creates epoch time.
    print 'Begin sleeping. #find a way to type commands while program sleeps or  find better method than time.sleep()'
    time.sleep(isnumber * 60) # pauses program for timelength minutes. numbers inside of the time.sleep() bracket are interpreted as seconds.
    end = time.time() # creates time signature for end time.
    apptimer = (end - start) / 60 # calculates the # of minutes by subtracting end from start and dividing by 60 (because it's in seconds).
    print 'It has been ' + str(apptimer) + ' minutes since program "fell asleep."'
    print "Time is up. Opening next task. "


#takes input from question "What would you like to do?" and pastes it into chrome search bar.
def chrome(url):
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url) #uses chrome to open url
    print "Opening webpage for " + str(isnumber) + " minutes."
    print "Don't you fucking dare get distracted you adhd piece of shit."


# main function
def main():

    #amasses input from user
    print "What would you like to do? (Enter url)"
    url = raw_input()
    print "How long would you like to work on this task?"
    timelength = raw_input()

    #where the magic happens
    isnumber(timelength)
    chrome(url)
    apptime(isnumber)

if __name__ == "__main__": #specifies to execute function if named main, i think?
    main() #executes function















#while timelength > 500 or timelength <= 0:
 #   print "Please enter a more realistic number, faggot."
  #  timelength = raw_input()











#def cycle:
 #   for x in range(time.sleep(minute))






















