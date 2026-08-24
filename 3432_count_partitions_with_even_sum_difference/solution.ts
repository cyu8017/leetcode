// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

export function countPartitions(nums: any): any {
    let total = 0;
    for (const x of nums) total += x;
    let ans = 0, left = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        left += nums[i];
        if ((left - (total - left)) % 2 === 0) ans++;
    }
    return ans;
}
