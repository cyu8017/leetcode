// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

int buyChoco(int* prices, int pricesSize, int money) {
    int a = 1000000000, b = 1000000000;
    for (int i = 0; i < pricesSize; i++) {
        int p = prices[i];
        if (p < a) { b = a; a = p; }
        else if (p < b) b = p;
    }
    if (a + b <= money) return money - a - b;
    return money;
}
