// LeetCode 2160 - Minimum Sum of Four Digit Number After Splitting Digits
// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

export function minimumSum(num: number): number {
    const d = [Math.floor(num / 1000), Math.floor(num / 100) % 10, Math.floor(num / 10) % 10, num % 10];
    d.sort((a, b) => a - b);
    return 10 * d[0] + d[2] + 10 * d[1] + d[3];
}
