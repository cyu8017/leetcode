// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution {
    public boolean checkZeroOnes(String s) {
        int maxZeros = 0;
        int maxOnes = 0;
        int zeros = 0;
        int ones = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '0') {
                zeros++;
                ones = 0;
                maxZeros = Math.max(maxZeros, zeros);
            } else {
                ones++;
                zeros = 0;
                maxOnes = Math.max(maxOnes, ones);
            }
        }

        return maxOnes > maxZeros;
    }
}
