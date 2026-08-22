// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

int countHousePlacements(int n) {
    const int mod = 1000000007;
    int a = 1, b = 1;
    for (int i = 1; i <= n; i++) {
        int na = (a + b) % mod;
        b = a;
        a = na;
    }
    int ways = (a + b) % mod;
    return (int)((long long)ways * ways % mod);
}
