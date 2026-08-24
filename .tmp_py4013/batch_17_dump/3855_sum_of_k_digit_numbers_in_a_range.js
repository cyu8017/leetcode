// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

function qpow(a, n, mod) {
    a %= mod;
    let ans = 1n;
    let A = BigInt(a), N = BigInt(n), MOD = BigInt(mod);
    let res = 1n;
    while (N > 0n) {
        if (N & 1n) res = res * A % MOD;
        A = A * A % MOD;
        N >>= 1n;
    }
    return Number(res);
}
var sumOfNumbers = function(l, r, k) {
    const MOD = 1000000007;
    const n = r - l + 1;
    let sum = Number((BigInt(l + r) * BigInt(n) / 2n) % BigInt(MOD));
    const part1 = qpow(n % MOD, k - 1, MOD);
    const part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD;
    const inv9 = qpow(9, MOD - 2, MOD);
    let ans = sum;
    ans = Number(BigInt(ans) * BigInt(part1) % BigInt(MOD));
    ans = Number(BigInt(ans) * BigInt(part2) % BigInt(MOD));
    ans = Number(BigInt(ans) * BigInt(inv9) % BigInt(MOD));
    return ans;
};
