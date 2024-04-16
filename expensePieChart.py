#CS175L
#Andrew Fisher
#expensePieChart

import matplotlib.pyplot as plt

def main():
    money = []
    slice_labels = []
    try:
        expenses = open('expenses.txt', 'r')
        for row in expenses:
            row = row.rstrip('\n')
            labels, values = row.split('\t')
            try:
                values = int(values)
                slice_labels.append(labels)
                money.append(values)
            except ValueError:
                print(f'{row}   error')
                continue

        plt.pie(money, labels=slice_labels)
        plt.title("Monthly Expenses")
        plt.show()

        expenses.close()

    except IOError:
        print('File not found')


if __name__ == '__main__':
    main()
