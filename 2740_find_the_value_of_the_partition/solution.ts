// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

export function findValueOfPartition(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 1; i < nums.length; i++) ans = Math.min(ans, nums[i] - nums[i - 1]);
    return ans;
}
