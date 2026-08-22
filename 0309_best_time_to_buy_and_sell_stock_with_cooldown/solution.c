// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

int maxProfit(int* prices, int pricesSize) {
    if (pricesSize == 0) {
        return 0;
    }
    int free = 0;
    int hold = -prices[0];
    int cooldown = 0;
    for (int index = 1; index < pricesSize; index++) {
        int price = prices[index];
        int nextFree = maxInt(free, cooldown);
        int nextHold = maxInt(hold, free - price);
        int nextCooldown = hold + price;
        free = nextFree;
        hold = nextHold;
        cooldown = nextCooldown;
    }
    return maxInt(free, cooldown);
}
