// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

export function minimumOperations(nums: any): any {
    let ops = 0;
    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] !== nums[i + 1]) ops++;
    }
    return ops;
}
