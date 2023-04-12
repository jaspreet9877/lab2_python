numberofYears = int(input("Enter the number of years: "))

Totalrainfall = [sum([float(input(f"Enter the rainfall for the year {year}, month {month} (in cm): ")) for month in range(1,13)]) for year in range(1, numberofYears+1)]
AverageRainfall = [total_rainfall/12 for total_rainfall in Totalrainfall]

print("\nYearly rainfall (in cm):")
for i, year_total in enumerate(Totalrainfall):
    print(f"Year {i+1}: {year_total:.2f}")

print("\nAverage monthly rainfall (in cm):")
for i, year_avg in enumerate(AverageRainfall):
    print(f"Year {i+1}: {year_avg:.2f}")
