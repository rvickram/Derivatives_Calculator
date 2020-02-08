# Created by: Ryan Vickramasinghe

# This code will calculate payoff and profit for an insured short position
# using a short position on an asset insured by a call option on that same
# asset.

# Get initial information from user:
initAssetValue = int(input('Enter asset value: '))
putStrikePrice = int(input('Enter strike price of put option: '))
putCost = int(input('Enter put option cost: '))
riskFreeIR = int(input('Enter risk-free interest rate (%): '))
# convert percentage to decimal:
riskFreeIR = riskFreeIR/100

while True:
    # get current asset price
    currAssetPrice = int(input('\nEnter current asset price: '))

    # if current price is greater than put strike, don't exercise
    if((currAssetPrice - putStrikePrice) >= 0):
        # payoff is simply the current price since we don't exercise
        payoff = currAssetPrice

        # calculate profit, factoring in intial invcestment and  put cost future value
        profit = currAssetPrice - (initAssetValue + putCost)*(1 + riskFreeIR)

    # if current price is LESS than initial price, we exercise the put
    else:
        # payoff is the put strike price
        payoff = putStrikePrice

        # profit
        profit = putStrikePrice - (initAssetValue + putCost)*(1 + riskFreeIR)
    
    print('Payoff: ' + str(payoff) + ' Profit: ' + str(profit))


    if(input('\nTry another price? (y/n): ') == 'n'):
        break

print(riskFreeIR)