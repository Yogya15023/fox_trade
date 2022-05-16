def invest(sl,stock_price,short_call,short_put,short_call_premium,short_put_premium):
    sum=short_call_premium+short_put_premium
    higher_strike=short_call+sum
    lower_strike=short_put-sum
    limiting_upside=stock_price+(stock_price*sl)/100
    limiting_downside=stock_price-(stock_price*sl)/100

    print("Higher strike plus total premium: ", higher_strike)
    print("Lower strike plus total premium: ", lower_strike)
    print("Limiting upside: ",limiting_upside)
    print("Limiting downside: ",limiting_downside)
    print("Net credit: ", sum)

sl=float(input("Enter the Sl: "))
stockPrice=float(input("Enter the stockprice: "))
shortCall=float(input("Enter the shortcall: "))
shortPut=float(input("Enter the shortput: "))
shortCallPremium=float(input("Enter the shortcallpremium: "))
shortPutPremium=float(input("Enter the shortputpremium: "))
invest(sl,stockPrice,shortCall,shortPut,shortCallPremium,shortPutPremium)
