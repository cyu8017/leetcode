// LeetCode 0461 - Hamming Distance
// https://leetcode.com/problems/hamming-distance/

class Solution {
    fun hammingDistance(x: Int, y: Int): Int {
        return (x xor y).countOneBits()
    }
}
