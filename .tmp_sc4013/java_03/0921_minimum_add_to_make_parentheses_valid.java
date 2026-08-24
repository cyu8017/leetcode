// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution {
    public int minAddToMakeValid(String s) {
        int openNeed = 0, closeNeed = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(') closeNeed++;
            else if (closeNeed > 0) closeNeed--;
            else openNeed++;
        }
        return openNeed + closeNeed;
    }
}
