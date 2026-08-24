// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

export function maximumDifference(nums: number[]): number {
    let ans = -1, mn = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > mn) ans = Math.max(ans, nums[i] - mn);
        else mn = nums[i];
    }
    return ans;
}
