def main():
    infile = open("clients.txt", "r")

    counter = 1
    for line in infile:
        print(counter, '. ', line.rstrip('\n'), sep=' ')
        counter += 1
    infile.close()
main()
