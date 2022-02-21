# Creating a dictionary from file data: {employee : {day : [start, end]}}
def order_data(file_name):
    file = open(file_name, 'r')
    office_time = {}
    for line in file:
        line = line.rstrip('\n').split('=')
        name = line[0]
        week = line[1].split(',')
        schedule = {}
        for day in week:
            hour = day[2:].split('-')
            start = hour[0].split(':')
            end = hour[1].split(':')
            # Creating intervals in minutes for each day
            schedule[day[0:2]] = [int(start[0])*60 + int(start[1]),
                                  int(end[0])*60 + int(end[1])]
        office_time[name] = schedule
    # print(office_time)
    file.close()
    return office_time


# Combination without repetitions
def combinator(office_time):
    workers = list(office_time.keys())
    for i in range(len(workers)-1):
        j = i+1
        while j < len(workers):
            coincidences = 0
            week_i = office_time[workers[i]]
            week_j = office_time[workers[j]]
            for day in week_i:
                if day in week_j:
                    start_i = week_i[day][0]
                    start_j = week_j[day][0]
                    end_i = week_i[day][1]
                    end_j = week_j[day][1]
                    if ((start_i == start_j and end_i == end_j)
                        or start_i < start_j < end_i
                        or start_j < start_i < end_j
                        or start_i < end_j < end_i
                        or start_j < end_i < end_j):
                        coincidences += 1
            print(workers[i], "-", workers[j], ": ", coincidences)
            j += 1


if __name__ == '__main__':
    office_data = order_data("input.txt")
    combinator(office_data)
