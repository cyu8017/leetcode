// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
    const best = new Map();
    let ans = -1;
    for (const v of nums) {
        let x = v, md = 0;
        while (x > 0) { md = Math.max(md, x % 10); x = Math.floor(x / 10); }
        if (best.has(md)) {
            ans = Math.max(ans, best.get(md) + v);
            best.set(md, Math.max(best.get(md), v));
        } else best.set(md, v);
    }
    return ans;
};
