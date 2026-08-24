// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

class Solution {
    fun finalString(s: String): String {
        var b = StringBuilder()
        for (c in s.toCharArray()) {
            if (c == 'i') b.reverse()
            else b.append(c)
        }
        return b.toString()
    }
}
