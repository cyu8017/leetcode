// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

class Solution {
    fun calculateTime(keyboard: String, word: String): Int {
        val pos = IntArray(26)
        for (i in keyboard.indices) pos[keyboard[i] - 'a'] = i
        var ans = 0
        var prev = 0
        for (ch in word) {
            ans += kotlin.math.abs(pos[ch - 'a'] - prev)
            prev = pos[ch - 'a']
        }
        return ans
    }
}
