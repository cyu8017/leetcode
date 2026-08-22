// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

int maxProfit(int* prices, int pricesSize, int fee) {
    int hold = -prices[0];
    int cash = 0;
    for (int i = 1; i < pricesSize; i++) {
        int price = prices[i];
        int newHold = hold > cash - price ? hold : cash - price;
        int newCash = cash > hold + price - fee ? cash : hold + price - fee;
        hold = newHold;
        cash = newCash;
    }
    return cash;
}
