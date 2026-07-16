// LeetCode 0122 - Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

int maxProfit(int* prices, int pricesSize) { int profit=0;for(int i=1;i<pricesSize;i++)if(prices[i]>prices[i-1])profit+=prices[i]-prices[i-1];return profit; }