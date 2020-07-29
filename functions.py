def add(x,y):
    return x+y

def product(x,y):
    return x*y

def test(x):
    return x


if __name__ == "__main__":
    lineList = [line.rstrip('\n') for line in open("test_parameters.txt")]
    processedList = []
    for line in lineList:
         res = tuple(map(int, line.split(','))) 
         processedList.append(res)
    print(processedList)