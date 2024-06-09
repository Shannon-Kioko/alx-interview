def makeChange(coins, total):
    if total == 0:
        return 0
    
    if (total < 0):
        return -1
    
    
    # dp_list = [float('inf') for i in range(total+1)]
    # dp_list[0] = 0

    # for i in range(len(dp_list)):
    #     for coin in coins:
    #         if i - coin >= 0:
    #             dp_list[i] = min(dp_list[i], dp_list[i-coin]+1)
    # return -1 if dp_list[-1] == float('inf') else dp_list[-1]


      

makeChange([2,3,5,4], 12)




