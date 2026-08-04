// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

/**
 * @param {number} n
 * @return {number}
 */
var countGoodNumbers = function(n) {
    const MOD = 1000000007n;
    const modPow = (base, exp) => {
        let r = 1n, b = BigInt(base), e = BigInt(exp);
        while (e > 0n) {
            if (e & 1n) r = r * b % MOD;
            b = b * b % MOD;
            e >>= 1n;
        }
        return r;
    };
    const nn = BigInt(n);
    return Number(modPow(5, (nn + 1n) / 2n) * modPow(4, nn / 2n) % MOD);
};
