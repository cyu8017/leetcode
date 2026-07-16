// LeetCode 0190 - Reverse Bits
// https://leetcode.com/problems/reverse-bits/

export function reverseBits(n: number): number {
    let result = 0;
    for (let bit = 0; bit < 32; bit++) {
        result = (result << 1) | (n & 1);
        n >>>= 1;
    }
    return result >>> 0;
}