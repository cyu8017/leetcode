// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

class Solution {
    fun canConvertString(s: String, t: String, k: Int): Boolean {
        if (s.length != t.length) return false
        val used = IntArray(26)
        for (i in s.indices) {
            val shift = (t[i] - s[i] + 26) % 26
            if (shift == 0) continue
            used[shift]++
            if (shift + 26L * (used[shift] - 1) > k) return false
        }
        return true
    }
}
