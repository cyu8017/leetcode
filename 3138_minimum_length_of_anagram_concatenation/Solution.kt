// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

class Solution {
    fun minAnagramLength(s: String): Int {
        var n = s.length
        var cnt = IntArray(26)
        for (i in 0 until n) { cnt[s[i] - 'a']++ }
        var i = 1
        while (true) {
            if (n % i == 0 && check(s, n, cnt, i)) return i
            i++
        }
    }

    private fun check(s: String, n: Int, cnt: IntArray, k: Int): Boolean {
        var i = 0
        while (i < n) {
            var cnt1 = IntArray(26)
            for (j in i until i + k) { cnt1[s[j] - 'a']++ }
            for (j in 0 until 26) {
                if (cnt1[j] * (n / k) != cnt[j]) return false
            }
            i += k
        }
        return true
    }
}
