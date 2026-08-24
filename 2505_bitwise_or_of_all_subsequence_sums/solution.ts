// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

export function subsequenceSumOr(nums: number[]): number {
    let ans = 0, prefix = 0;
    for (const x of nums) {
        prefix += x;
        ans |= x | prefix;
    }
    return ans;
}
