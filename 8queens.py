 #!usr/bin/env pyhon3

def queen(li):
    for n in range(10):
        oindex= 9-n
        #print(li)
        if n == 0 or n == 9:
            print("+-----------------+")
        else:
            for i in range(9):
                if i == 0:
                    print("| ",end="")

                elif li[i-1] == 8-n:
                    print("Q ",end="")
                else:
                   print(". ",end="")

                if i == 8:
                    print("|")

                        


def main():

    queen([0,4,7,5,2,6,1,3])

#############################################################################

if __name__ == '__main__':
    main()


