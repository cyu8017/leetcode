// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

class Solution {
    public boolean hasMatch(String s, String p) {
        int i = p.indexOf('*');
        String left = p.substring(0, i);
        String right = p.substring(i + 1);
        int li = s.indexOf(left);
        if (li < 0) return false;
        return s.indexOf(right, li + left.length()) >= 0;
    }
}
