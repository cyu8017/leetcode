// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

export function countSubarrays(nums: number[]): number {
    let ans = 0, len = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] > nums[i - 1]) len++;
        else len = 1;
        ans += len;
    }
    return ans;
}
