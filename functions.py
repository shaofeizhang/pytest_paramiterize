import parameters


def add(x,y):
    return x+y

def product(x,y):
    return x*y

def test(x):
    return x

def test1(x,y):
    return x+y

def test2(x):
    return x

def test3(x,y):
    return x*y

def add3String(x,y,z):
    return x+y+z


if __name__ == "__main__":
    person = parameters.Inputs()
    print(person.input_suite1)