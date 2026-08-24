// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

export function xorBeauty(nums: number[]): number {
    let ans = 0;
    for (const x of nums) ans ^= x;
    return ans;
}
