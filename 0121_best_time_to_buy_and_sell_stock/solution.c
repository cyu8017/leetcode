// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

int maxProfit(int* prices, int pricesSize) { int low=2147483647,best=0;for(int i=0;i<pricesSize;i++){if(prices[i]<low)low=prices[i];if(prices[i]-low>best)best=prices[i]-low;}return best; }