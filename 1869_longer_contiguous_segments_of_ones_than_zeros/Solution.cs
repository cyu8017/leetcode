// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

public class Solution {
    public bool CheckZeroOnes(string s) {
        int maxZeros = 0;
        int maxOnes = 0;
        int zeros = 0;
        int ones = 0;
        foreach (char ch in s) {
            if (ch == '0') {
                zeros++;
                ones = 0;
                maxZeros = Math.Max(maxZeros, zeros);
            } else {
                ones++;
                zeros = 0;
                maxOnes = Math.Max(maxOnes, ones);
            }
        }
        return maxOnes > maxZeros;
    }
}
