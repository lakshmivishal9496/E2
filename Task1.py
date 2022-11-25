def get_value(filename):
    infile = open(filename, 'r')
    contents = infile.readlines()
    list1 = []
    for items in contents:
        list1.append(float(items.rstrip('\n')))
    infile.close()
    return list1


def main():
    filenames = ['morning.txt', 'afternoon.txt']
    measurement = []
    for filename in filenames:
        value = get_value(filename)
        measurement += value
    print(measurement)


main()
