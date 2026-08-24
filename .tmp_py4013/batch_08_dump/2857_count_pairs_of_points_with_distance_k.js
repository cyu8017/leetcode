// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

/**
 * @param {number[][]} coordinates
 * @param {number} k
 * @return {number}
 */
var countPairs = function(coordinates, k) {
    const freq = new Map();
    const key = (x, y) => (BigInt(x) << 32n) ^ BigInt(y >>> 0);
    let ans = 0;
    for (const [x, y] of coordinates) {
        for (let a = 0; a <= k; a++) {
            const b = k - a;
            ans += freq.get(key(x ^ a, y ^ b).toString()) || 0;
        }
        const k0 = key(x, y).toString();
        freq.set(k0, (freq.get(k0) || 0) + 1);
    }
    return ans;
};
