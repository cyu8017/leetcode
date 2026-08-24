// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    const ans = new Array(nums.length);
    let pos = 0, neg = 1;
    for (const x of nums) {
        if (x > 0) { ans[pos] = x; pos += 2; }
        else { ans[neg] = x; neg += 2; }
    }
    return ans;
};
