// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

export function maximizeSum(nums: any, k: any): any {
    let mx = nums[0];
    for (const x of nums) if (x > mx) mx = x;
    return k * mx + k * (k - 1) / 2;
}
