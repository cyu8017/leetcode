// LeetCode 0231 - Power of Two
// https://leetcode.com/problems/power-of-two/

export function isPowerOfTwo(n: number): boolean {
    return n > 0 && (n & (n - 1)) === 0;
}
