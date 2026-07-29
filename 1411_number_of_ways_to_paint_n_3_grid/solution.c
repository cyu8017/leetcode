// LeetCode 1411 - Number of Ways to Paint N x 3 Grid
// https://leetcode.com/problems/number-of-ways-to-paint-n-x-3-grid/

int numOfWays(int n) {
    const int MOD = 1000000007;
    long long aba = 6, abc = 6;
    for (int i = 1; i < n; i++) {
        long long naba = (3 * aba + 2 * abc) % MOD;
        long long nabc = (2 * aba + 2 * abc) % MOD;
        aba = naba; abc = nabc;
    }
    return (int)((aba + abc) % MOD);
}
