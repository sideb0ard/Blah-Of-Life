import sys

# def biggest(*args):


def Main(argv):
    num_numz = len(argv)
    biggest = 0
    if num_numz > 1:
        while (num_numz > 1):
            if int(argv[num_numz - 1]) > biggest:
                biggest = int(argv[num_numz - 1])
            num_numz -= 1

    return biggest

if __name__ == "__main__":
    biggest = Main(sys.argv)
    print("Biigest", biggest)
