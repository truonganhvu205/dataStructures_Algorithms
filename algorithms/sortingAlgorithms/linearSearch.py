def linearSearch(numberList, numberToFind):
    for index, element in enumerate(numberList):
        if element == numberToFind:
            return index

    return -1

if __name__ == '__main__':
    numberList = [1, 3, 5, 7, 9, 8, 6, 4, 2]
    numberToFind = 8

    print(linearSearch(numberList, numberToFind))
    