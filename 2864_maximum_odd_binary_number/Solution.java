// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

class Solution {
    public String maximumOddBinaryNumber(String s) {
        int ones = 0;
        for (int i = 0; i < s.length(); i++) if (s.charAt(i) == '1') ones++;
        int zeros = s.length() - ones;
        StringBuilder b = new StringBuilder(s.length());
        for (int i = 0; i < ones - 1; i++) b.append('1');
        for (int i = 0; i < zeros; i++) b.append('0');
        b.append('1');
        return b.toString();
    }
}
