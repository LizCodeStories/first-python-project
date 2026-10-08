def getdata():
    population = []

    file = open("USPopulation.txt", "r")

    for line in file:
        population.append(int(line.strip()))

    file.close()

    return population


def putdata(data):
    for value in data:
        print(value)


def find_increase(population):
    annual_increase = []

    for i in range(1, len(population)):
        increase = population[i] - population[i - 1]
        annual_increase.append(increase)

    return annual_increase


def analyze_data(annual_increase):
    highest = max(annual_increase)
    smallest = min(annual_increase)
    average = sum(annual_increase) / 40

    highest_index = annual_increase.index(highest)
    smallest_index = annual_increase.index(smallest)

    highest_year = 1951 + highest_index
    smallest_year = 1951 + smallest_index

    print("Highest increase:", highest, "in", highest_year)
    print("Smallest increase:", smallest, "in", smallest_year)
    print("Average increase:", average)


def find_acceleration(annual_increase):
    acceleration = []

    for i in range(1, len(annual_increase)):
        difference = annual_increase[i] - annual_increase[i - 1]
        acceleration.append(difference)

    return acceleration


def main():
    population = getdata()

    print("Population:")
    putdata(population)

    annual_increase = find_increase(population)

    print("Annual Increase:")
    putdata(annual_increase)

    analyze_data(annual_increase)

    acceleration = find_acceleration(annual_increase)

    print("Acceleration/Deceleration:")
    putdata(acceleration)


main()