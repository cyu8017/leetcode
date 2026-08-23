// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

/**
 * @param {number[]} nums
 * @return {number}
 */
var alternatingSubarray = function(nums) {
    let ans = -1;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const expect = ((j - i) % 2 === 0) ? -1 : 1;
            if (nums[j] - nums[j - 1] !== expect) break;
            if (nums[i + 1] - nums[i] !== 1) break;
            ans = Math.max(ans, j - i + 1);
        }
    }
    return ans;
};
