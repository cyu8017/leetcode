// LeetCode 0191 - Number of 1 Bits
// https://leetcode.com/problems/number-of-1-bits/

export function hammingWeight(n: number): number {
    let count = 0;
    while (n) {
        n &= n - 1;
        count++;
    }
    return count;
}