// LeetCode 0441 - Arranging Coins
// https://leetcode.com/problems/arranging-coins/

int arrangeCoins(int n) {
    long long low = 0;
    long long high = n;
    while (low <= high) {
        long long mid = (low + high) / 2;
        if (mid * (mid + 1) / 2 <= n) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return (int)high;
}
