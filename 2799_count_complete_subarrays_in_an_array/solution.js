// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countCompleteSubarrays = function(nums) {
    const need = new Set(nums).size;
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const seen = new Set();
        for (let j = i; j < n; j++) {
            seen.add(nums[j]);
            if (seen.size === need) {
                ans += n - j;
                break;
            }
        }
    }
    return ans;
};
