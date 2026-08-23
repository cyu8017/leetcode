// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

class Solution {
    public String largestEven(String s) {
        while (s.length() > 0 && s.charAt(s.length() - 1) == '1') s = s.substring(0, s.length() - 1);
        return s;
    }
}
