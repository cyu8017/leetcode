// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPairs = function(nums, k) {
    const gcd = (a, b) => {
        while (b !== 0) { const t = a % b; a = b; b = t; }
        return a;
    };
    const freq = new Map();
    let ans = 0;
    for (const x of nums) {
        const g1 = gcd(x, k);
        for (const [g2, cnt] of freq)
            if ((g1 * g2) % k === 0) ans += cnt;
        freq.set(g1, (freq.get(g1) || 0) + 1);
    }
    return ans;
};
