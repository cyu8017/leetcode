// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

class Solution {
    fun isContiguous(a: Char, b: Char): Boolean {
        var x = kotlin.math.abs(a - b)
        return x == 1 || x == 25
    }
    fun resultingString(s: String): String {
        var stk = StringBuilder()
        for (c in s.toCharArray()) {
            if (stk.length() > 0 && isContiguous(stk.charAt(stk.length() - 1), c))
                stk.deleteCharAt(stk.length - 1)
            else stk.append(c)
        }
        return stk.toString()
    }
}
