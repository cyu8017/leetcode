// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution {
    fun minAddToMakeValid(s: String): Int {
        var openNeed = 0
        var closeNeed = 0
        for (ch in s) {
            if (ch == '(') closeNeed++
            else if (closeNeed > 0) closeNeed--
            else openNeed++
        }
        return openNeed + closeNeed
    }
}
