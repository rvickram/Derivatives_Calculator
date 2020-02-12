# By Ryan Vickramasinghe

def call_payoff(strike, premium, currentPrice):
    priceDiff = max(0, currentPrice - strike)

    # if the current price is higher than strike, exercise
    if(priceDiff > 0):
        return priceDiff
    # otherwise don't exercise option
    else:
        return 0


def call_profit(strike, premium, currentPrice):
    priceDiff = max(0, currentPrice - strike)

    # if the current price is higher than strike, profit is diff.
    # between strike and current price minus the option premium
    if (priceDiff > 0):
        return priceDiff - premium
    # otherwise we don't exercise and we lose just the premium
    else:
        return -1*premium


strike = int(input('Enter strike price: '))
premium = int(input('Enter option premium: '))
currentPrice = int(input('Enter current price: '))

print('Payoff is: ' + str(call_payoff(strike, premium, currentPrice)))
print('Profit is: ' + str(call_profit(strike, premium, currentPrice)))