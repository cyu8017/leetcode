// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

export function sumOfSquares(nums: number[]): number {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (n % (i + 1) === 0) ans += nums[i] * nums[i];
    }
    return ans;
}
