#CS175L
#Andrew Fisher
#AverageFromInput

def main():
    total = 0
    num = 0
    totalnums = 0
    num_file = open('numbers.txt', 'r')
    for i in num_file:
        totalnums += 1
        num = float(i)
        total = total + num
        print(f'I read in  {totalnums} number(s) Current number is:   {num:6.2f} Total is:   {total:6.2f}')

    average = total / totalnums
    print(f'Average is: {average}')

    num_file.close()


if __name__ == '__main__':
    main()

    
