// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    const n = nums.length;
    if (n === 1) return 0;
    const top2 = (idxs) => {
        const freq = new Map();
        for (const i of idxs) freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
        let a = 0, ac = 0, b = 0, bc = 0;
        for (const [v, c] of freq) {
            if (c > ac) { b = a; bc = ac; a = v; ac = c; }
            else if (c > bc) { b = v; bc = c; }
        }
        return [a, ac, b, bc];
    };
    const even = [], odd = [];
    for (let i = 0; i < n; i++) (i % 2 === 0 ? even : odd).push(i);
    const e = top2(even);
    const o = top2(odd);
    if (e[0] !== o[0]) return n - e[1] - o[1];
    return Math.min(n - e[1] - o[3], n - e[3] - o[1]);
};
