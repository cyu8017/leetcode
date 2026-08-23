// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

/**
 * @param {number} n
 * @return {number}
 */
var stringCount = function(n) {
    if (n < 4) return 0;
    const MOD = 1000000007n;
    const modPow = (a, b) => {
        let res = 1n;
        a %= MOD;
        let bb = BigInt(b);
        while (bb > 0n) {
            if (bb & 1n) res = (res * a) % MOD;
            a = (a * a) % MOD;
            bb >>= 1n;
        }
        return res;
    };
    const nn = BigInt(n);
    let ans = modPow(26n, n);
    ans = (ans - 3n * modPow(25n, n) % MOD + MOD) % MOD;
    ans = (ans + 3n * modPow(24n, n) % MOD) % MOD;
    ans = (ans - modPow(23n, n) + MOD) % MOD;
    ans = (ans + nn % MOD * modPow(25n, n - 1) % MOD) % MOD;
    ans = (ans - 2n * (nn % MOD) % MOD * modPow(24n, n - 1) % MOD + MOD) % MOD;
    ans = (ans + nn % MOD * modPow(23n, n - 1) % MOD) % MOD;
    ans = (ans - nn % MOD * ((nn - 1n + MOD) % MOD) % MOD * modPow(24n, n - 2) % MOD % MOD + MOD) % MOD;
    ans = (ans + nn % MOD * ((nn - 1n + MOD) % MOD) % MOD * modPow(23n, n - 2) % MOD) % MOD;
    return Number(ans);
};
