// LeetCode 0461 - Hamming Distance
// https://leetcode.com/problems/hamming-distance/

using System.Numerics;

public class Solution {
    public int HammingDistance(int x, int y) {
        return BitOperations.PopCount((uint)(x ^ y));
    }
}
