// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

function modPow(a, e, mod) {
    let r = 1;
    a %= mod;
    while (e > 0) {
        if (e & 1) r = r * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return r;
}
var numberOfWays = function(n, x, y) {
    const mod = 1000000007;
    const dp = Array.from({length: n + 1}, () => new Array(x + 1).fill(0));
    dp[0][0] = 1;
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= x && j <= i; j++) {
            dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j] % mod) % mod;
        }
    }
    const fact = new Array(x + 1);
    fact[0] = 1;
    for (let i = 1; i <= x; i++) fact[i] = fact[i - 1] * i % mod;
    let ans = 0, ypow = 1;
    for (let k = 1; k <= x && k <= n; k++) {
        ypow = ypow * y % mod;
        const perm = fact[x] * modPow(fact[x - k], mod - 2, mod) % mod;
        ans = (ans + dp[n][k] * perm % mod * ypow % mod) % mod;
    }
    return ans;
};
