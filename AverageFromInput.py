#CS175L
#Andrew Fisher
#AverageFromInput

def main():
    total = 0
    num = 0
    totalnums = 0
    
    try:
        num_file = open('numbers.txt', 'r')
        for i in num_file:
            try:
                num = float(i)
                totalnums += 1
                total = total + num
                print(f'I read in  {totalnums} number(s) Current number is:   {num:6.2f} Total is:   {total:6.2f}')
            except ValueError:
                i = i.strip()
                print(f'Bad data: {i} skipping')
                
        num_file.close()

        average = total / totalnums
        print(f'Average is: {average}')

    except IOError:
        import sys
        sys.exit("File not found: numbers.txt - exiting")


if __name__ == '__main__':
    main()

    
