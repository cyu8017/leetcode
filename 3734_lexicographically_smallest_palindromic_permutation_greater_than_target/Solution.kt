// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically_smallest_palindromic_permutation_greater_than_target/

class Solution {
    private var half: IntArray? = null
    private var left: CharArray? = null
    private var target: String? = null
    private var halfLen: Int = 0
    private var mid: Int = 0

    fun lexPalindromicPermutation(s: String, target: String): String {
        var cnt = IntArray(26)
        for (c in s.toCharArray()) { cnt[c - 'a']++ }
        var odd = 0
        mid = -1
        for (i in 0 until 26) {
            if (cnt[i] % 2 == 1) { odd += 1; mid = i; }
        }
        if (odd > 1) return ""
        half = IntArray(26)
        for (i in 0 until 26) { half[i] = cnt[i] / 2 }
        var n = s.length
        halfLen = n / 2
        this.target = target
        left = CharArray(halfLen)
        if (!dfs(0, false)) return ""
        var res = StringBuilder()
        res.append(left)
        if (mid >= 0) res.append(('a' + mid).toInt().toChar())
        run {
            var i = halfLen - 1
            while (i >= 0) {
                res.append(left[i])
                i = i - 1
            }
        }
        var out = res.toString()
        if (out.compareTo(target) <= 0) return ""
        return out
    }

    private fun dfs(pos: Int, greater: Boolean): Boolean {
        if (pos == halfLen) {
            if (mid >= 0) {
                if (greater) return true
                return ('a' + mid).toInt().toChar() > target[halfLen]
            }
            return greater
        }
        var start = if (greater) 0 else (target[pos] - 'a')
        for (c in start until 26) {
            if (half[c] == 0) continue
            half[c]--
            left[pos] = ('a' + c).toInt().toChar()
            if (dfs(pos + 1, greater || c > (target[pos] - 'a'))) return true
            half[c]++
        }
        return false
    }
}
