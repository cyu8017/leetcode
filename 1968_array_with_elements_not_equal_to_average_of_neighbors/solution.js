// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length;
    const mid = Math.floor((n + 1) / 2);
    const small = nums.slice(0, mid), large = nums.slice(mid);
    const ans = [];
    let i = 0, j = 0;
    while (i < small.length || j < large.length) {
        if (i < small.length) ans.push(small[i++]);
        if (j < large.length) ans.push(large[j++]);
    }
    return ans;
};
