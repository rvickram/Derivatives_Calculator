# Created by: Ryan Vickramasinghe

# This code will calculate payoff and profit for an insured short position
# using a short position on an asset insured by a call option on that same
# asset.

# Get initial information from user:
initAssetValue = int(input('Enter asset value: '))
callStrikePrice = int(input('Enter strike price of call option: '))
callCost = int(input('Enter call option cost: '))
riskFreeIR = int(input('Enter risk-free interest rate (%): '))
# convert percentage to decimal:
riskFreeIR = riskFreeIR/100

while True:
    # get current asset price
    currAssetPrice = int(input('\nEnter current asset price: '))

    # if current price is less than call strike, don't exercise
    if((currAssetPrice - callStrikePrice) <= 0):
        # payoff is simply the current price since we don't exercise
        # (although negative since we must sell for that price)
        payoff = -1*currAssetPrice

        # calculate profit, factoring in intial invcestment and  put cost future value
        profit = payoff - (-1*callStrikePrice + callCost)*(1 + riskFreeIR)

    # if current price is LESS than initial price, we exercise the put
    else:
        # payoff is the put strike price
        payoff = -1*callStrikePrice

        # profit
        profit = payoff - (-1*initAssetValue + callCost)*(1 + riskFreeIR)
    
    print('Payoff: ' + str(payoff) + ' Profit: ' + str(profit))


    if(input('\nTry another price? (y/n): ') == 'n'):
        break

print('\nClosed program.')