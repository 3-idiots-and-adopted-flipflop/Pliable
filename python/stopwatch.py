import time
def time_convert(sec):
    min=sec//60 #getting whole number for minutes
    hr = min//60  #getting whole number for hours
    sec = sec % 60 #the  remainder of the division is used as seconds
    print("Time Lapsed = {0}:{1}:{2}".format(int(hr),int(min),round(sec)))



input("Press Enter to start")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time

time_convert(time_lapsed)


