// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

export function isIdealPermutation(nums: number[]): boolean {
    for (let i = 0; i < nums.length; i++) {
        if (Math.abs(nums[i] - i) > 1) return false;
    }
    return true;
}
