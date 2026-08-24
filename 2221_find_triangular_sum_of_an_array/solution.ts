// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

export function triangularSum(nums: number[]): number {
    while (nums.length > 1) {
        const next = new Array(nums.length - 1);
        for (let i = 0; i < next.length; i++)
            next[i] = (nums[i] + nums[i + 1]) % 10;
        nums = next;
    }
    return nums[0];
}
