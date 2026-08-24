// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

export function partitionArray(nums: any, k: any): any {
    nums.sort((a, b) => a - b);
    let ans = 1, start = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] - start > k) { ans++; start = nums[i]; }
    }
    return ans;
}
