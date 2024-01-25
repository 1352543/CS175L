#CS175L
#Andrew Fisher
#Stocks

commissionRatePurchase = float(input('Enter commission rate percentage on stock purchase: '))
commissionRateSale = float(input('Enter commission rate percentage on stock sale: '))
numSharesPurchased = int(input('Enter number of shares purchased: '))
numSharesSold = int(input('Enter number of shares sold: '))
purchasePrice = float(input('Enter purchase price per share: '))
salePrice = float(input('Enter sell price per share: '))

amountPaidForStock = 0.0
purchaseCommission = 0.0
totalPaid = 0.0
stockSoldFor = 0.0
sellingCommission = 0.0
totalReceived = 0.0
profitForSale = 0.0

amountPaidForStock = numSharesPurchased * purchasePrice
purchaseCommission = commissionRatePurchase * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = numSharesSold * salePrice
sellingCommission = commissionRateSale * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitForSale = totalReceived - totalPaid

print('')
print(f'Amount paid for the stock: ${amountPaidForStock:,.2f}')
print(f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print(f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print(f'Commission paid on the sale: ${sellingCommission:,.2f}')
print(f'Profit (or loss if negative): ${profitForSale:,.2f}')
