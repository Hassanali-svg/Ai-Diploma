import traceback

#This line opens a log file
with open("log.txt", "w") as log:

    try:
        
        print("Creating DB Connection", file = log)
    except Exception:
        traceback.print_exc(file=log)
