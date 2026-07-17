// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

/**
 * @param {number[][]} queries
 * @return {number[]}
 */
var waysToFillArray = function(queries) {
    const MOD = 1000000007n;
    const powMod = (base, exp) => {
        let result = 1n;
        base %= MOD;
        while (exp > 0n) {
            if (exp & 1n) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1n;
        }
        return result;
    };
    const combMod = (a, b) => {
        let num = 1n;
        let den = 1n;
        for (let i = 1n; i <= b; i++) {
            num = num * ((a - b + i) % MOD) % MOD;
            den = den * i % MOD;
        }
        return num * powMod(den, MOD - 2n) % MOD;
    };
    const ans = [];
    for (const [n, k] of queries) {
        let ways = 1n;
        let value = k;
        let d = 2;
        while (d * d <= value) {
            if (value % d === 0) {
                let exp = 0;
                while (value % d === 0) {
                    value = Math.floor(value / d);
                    exp++;
                }
                ways = ways * combMod(BigInt(n + exp - 1), BigInt(exp)) % MOD;
            }
            d += d === 2 ? 1 : 2;
        }
        if (value > 1) {
            ways = ways * BigInt(n) % MOD;
        }
        ans.push(Number(ways));
    }
    return ans;
};
