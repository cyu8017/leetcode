// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

class Solution {
    fun takeCharacters(s: String, k: Int): Int {
        val n = s.length
        val cnt = IntArray(3)
        for (c in s) cnt[c - 'a']++
        if (cnt[0] < k || cnt[1] < k || cnt[2] < k) return -1
        val need = intArrayOf(cnt[0] - k, cnt[1] - k, cnt[2] - k)
        val window = IntArray(3)
        var left = 0
        var maxMid = 0
        for (right in 0 until n) {
            window[s[right] - 'a']++
            while (window[0] > need[0] || window[1] > need[1] || window[2] > need[2]) {
                window[s[left] - 'a']--
                left++
            }
            if (right - left + 1 > maxMid) maxMid = right - left + 1
        }
        return n - maxMid
    }
}
