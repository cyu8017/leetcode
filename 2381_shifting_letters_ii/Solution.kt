// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

class Solution {
    fun shiftingLetters(s: String, shifts: Array<IntArray>): String {
        val n = s.length
        val diff = IntArray(n + 1)
        for (sh in shifts) {
            val d = if (sh[2] == 0) -1 else 1
            diff[sh[0]] += d
            diff[sh[1] + 1] -= d
        }
        val arr = s.toCharArray()
        var cur = 0
        for (i in 0 until n) {
            cur = (cur + diff[i]) % 26
            if (cur < 0) cur += 26
            arr[i] = ('a' + (arr[i] - 'a' + cur) % 26)
        }
        return String(arr)
    }
}
