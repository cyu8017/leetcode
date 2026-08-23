// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

/**
 * @param {number[]} deliciousness
 * @return {number}
 */
var countPairs = function(deliciousness) {
    const mod = 1000000007;
    const seen = new Map();
    let ans = 0;
    for (const value of deliciousness) {
        for (let power = 0; power < 22; power++) {
            const target = (1 << power) - value;
            const count = seen.get(target);
            if (count !== undefined) {
                ans += count;
            }
        }
        seen.set(value, (seen.get(value) ?? 0) + 1);
    }
    return ans % mod;
};
