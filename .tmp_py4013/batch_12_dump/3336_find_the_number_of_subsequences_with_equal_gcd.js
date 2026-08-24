// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

function gcd(a, b) {
    if (a === 0) return b;
    while (b !== 0) { const t = a % b; a = b; b = t; }
    return a;
}
var subsequencePairCount = function(nums) {
    const mod = 1000000007;
    let maxV = 0;
    for (const x of nums) if (x > maxV) maxV = x;
    let dp = Array.from({length: maxV + 1}, () => new Array(maxV + 1).fill(0));
    dp[0][0] = 1;
    for (const x of nums) {
        const ndp = Array.from({length: maxV + 1}, () => new Array(maxV + 1).fill(0));
        for (let a = 0; a <= maxV; a++) {
            for (let b = 0; b <= maxV; b++) ndp[a][b] = dp[a][b];
        }
        for (let a = 0; a <= maxV; a++) {
            for (let b = 0; b <= maxV; b++) {
                if (dp[a][b] === 0) continue;
                const na = a === 0 ? x : gcd(a, x);
                const nb = b === 0 ? x : gcd(b, x);
                ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod;
                ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod;
            }
        }
        dp = ndp;
    }
    let ans = 0;
    for (let g = 1; g <= maxV; g++) ans = (ans + dp[g][g]) % mod;
    return ans;
};
