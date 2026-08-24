// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

export function findClosestNumber(nums: number[]): number {
    let ans = nums[0];
    for (const x of nums) {
        if (Math.abs(x) < Math.abs(ans) || (Math.abs(x) === Math.abs(ans) && x > ans)) ans = x;
    }
    return ans;
}
