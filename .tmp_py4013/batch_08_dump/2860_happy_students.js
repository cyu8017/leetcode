// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countWays = function(nums) {
    nums = [...nums].sort((a, b) => a - b);
    const n = nums.length;
    let ans = 0;
    if (nums[0] > 0) ans++;
    for (let i = 0; i < n; i++) {
        const selected = i + 1;
        if (selected > nums[i] && (i === n - 1 || selected < nums[i + 1])) ans++;
    }
    return ans;
};
