def first(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive")
            return value
        except ValueError as error:
            print(error)

def speciesData(start_count, daily_increase, num_days):
    current_count = start_count
    print("Day 01 count:", current_count)
    for day in range(2, num_days+1):
        current_count += current_count * daily_increase / 100
        print(f"Day {day:02d} count: {int(current_count)}")

firstCount = first("Enter starting number of organisms/species: ")
increase = first("Enter average daily percentage increase: ")
numberofdays = first("Enter how many days' worth of data to be printed: ")

speciesData(firstCount, increase, numberofdays)
