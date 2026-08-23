// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countHillValley = function(nums) {
    const compact = [nums[0]];
    for (let i = 1; i < nums.length; i++)
        if (nums[i] !== compact[compact.length - 1]) compact.push(nums[i]);
    let ans = 0;
    for (let i = 1; i + 1 < compact.length; i++)
        if ((compact[i] > compact[i - 1] && compact[i] > compact[i + 1]) ||
            (compact[i] < compact[i - 1] && compact[i] < compact[i + 1]))
            ans++;
    return ans;
};
