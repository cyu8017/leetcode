// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

class Solution {
    private fun calc1(s: String): Int {
        var res = 0
        val n = s.length
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n && s[j] == s[i]) j++
            res = maxOf(res, j - i)
            i = j
        }
        return res
    }

    private fun calc2(s: String, a: Char, b: Char): Int {
        var res = 0
        val n = s.length
        var i = 0
        while (i < n) {
            while (i < n && s[i] != a && s[i] != b) i++
            val pos = HashMap<Int, Int>()
            pos[0] = i - 1
            var d = 0
            while (i < n && (s[i] == a || s[i] == b)) {
                if (s[i] == a) d++ else d--
                if (pos.containsKey(d)) res = maxOf(res, i - pos[d]!!)
                else pos[d] = i
                i++
            }
        }
        return res
    }

    private fun calc3(s: String): Int {
        val pos = HashMap<Long, Int>()
        pos[0L] = -1
        val cnt = IntArray(3)
        var res = 0
        for (i in s.indices) {
            cnt[s[i] - 'a']++
            val x = cnt[0] - cnt[1]
            val y = cnt[1] - cnt[2]
            val k = (x.toLong() shl 32) xor (y.toLong() and 0xffffffffL)
            if (pos.containsKey(k)) res = maxOf(res, i - pos[k]!!)
            else pos[k] = i
        }
        return res
    }

    fun longestBalanced(s: String): Int {
        val x = calc1(s)
        val y = maxOf(calc2(s, 'a', 'b'), maxOf(calc2(s, 'b', 'c'), calc2(s, 'a', 'c')))
        val z = calc3(s)
        return maxOf(x, maxOf(y, z))
    }
}
