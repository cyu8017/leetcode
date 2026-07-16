class Solution:
    def maxProfit(self, inventory, orders):
        MOD=1000000007; inventory.sort(reverse=True); inventory.append(0); ans=0
        for i in range(len(inventory)-1):
            width=i+1; high,low=inventory[i],inventory[i+1]; balls=width*(high-low)
            take=min(orders,balls); full,rem=divmod(take,width)
            bottom=high-full
            ans += width*(high+bottom+1)*full//2 + rem*bottom
            orders-=take
            if orders==0: break
        return ans%MOD
