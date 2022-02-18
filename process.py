log_file = open("um-server-01.txt") # this opens the data in um-server-01 to make it available to us


def sales_reports(log_file): # function sales_reports taking in the argument of log_file
    for line in log_file: # looping through the data
        line = line.rstrip() # removes whitespace
        day = line[0:3] # selecting 0 index where the day is located in um-server-01.txt
        if day == "Mon": # selecting day of line to print
            print(line) # console logging the lines

def melon_delivers(log_file):
    for line in log_file:
        row = line.split('')
        answer = row[0:4]
        mels = int(answer[2])
        if mels > 10:
            print(row)


sales_reports(log_file) # invoking the function
