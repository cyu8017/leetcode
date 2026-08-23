// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

/**
 * @param {number} n
 * @return {number}
 */
var monkeyMove = function(n) {
    const MOD = 1000000007;
    const powMod = (a, e) => {
        let res = 1;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    };
    return (powMod(2, n) - 2 + MOD) % MOD;
};
