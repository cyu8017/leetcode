// LeetCode 0461 - Hamming Distance
// https://leetcode.com/problems/hamming-distance/

class Solution {
    hammingDistance(x, y) {
        let xor = x ^ y;
        let count = 0;
        while (xor) {
            count += xor & 1;
            xor >>>= 1;
        }
        return count;
    }
}

module.exports = { Solution };
