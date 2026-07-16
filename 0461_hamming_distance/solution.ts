// LeetCode 0461 - Hamming Distance
// https://leetcode.com/problems/hamming-distance/

export class Solution {
    hammingDistance(x: number, y: number): number {
        let xor = x ^ y;
        let count = 0;
        while (xor) {
            count += xor & 1;
            xor >>>= 1;
        }
        return count;
    }
}
