// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

function buildArray(nums: number[]): number[] {
    return nums.map((x: any) => nums[x]);
}
