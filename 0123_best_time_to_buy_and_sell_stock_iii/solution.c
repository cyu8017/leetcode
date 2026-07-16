// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

int maxProfit(int* prices, int pricesSize) { int b1=2147483647,b2=2147483647,s1=0,s2=0;for(int i=0;i<pricesSize;i++){int p=prices[i];if(p<b1)b1=p;if(p-b1>s1)s1=p-b1;if(p-s1<b2)b2=p-s1;if(p-b2>s2)s2=p-b2;}return s2; }