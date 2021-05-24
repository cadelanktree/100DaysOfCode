def main():
    while(True):
        test = raw_input("Enter in 1 to continue, 2 to quit loop.")
        """ Testing how to exit from while(True) loop """
        if test == "1":
            continue
        elif test == "2":
            return False
        else:
            continue

if __name__ == "__main__":
    main()
