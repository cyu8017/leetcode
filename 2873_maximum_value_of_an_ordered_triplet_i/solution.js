// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++)
        for (let j = i + 1; j < n; j++)
            for (let k = j + 1; k < n; k++) {
                const cand = (nums[i] - nums[j]) * nums[k];
                if (cand > ans) ans = cand;
            }
    return ans;
};
