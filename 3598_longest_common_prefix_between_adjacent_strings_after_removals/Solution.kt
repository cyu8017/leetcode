// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

class Solution {
    var words: Array<String>? = null
    var n = 0
    var tm = TreeMap<Int, Int>()

    fun calc(s: String, t: String): Int {
        var m = minOf(s.length, t.length)
        for (k in 0 until m) { if (s[k] != t[k]) return k }
        return m
    }

    fun add(i: Int, j: Int) {
        if (i >= 0 && i < n && j >= 0 && j < n) tm.merge(calc(words[i], words[j]), 1, Integer::sum)
    }

    fun remove(i: Int, j: Int) {
        if (i >= 0 && i < n && j >= 0 && j < n) {
            var x = calc(words[i], words[j])
            var c = tm[x]
            if (c == 1) tm.remove(x)
            else tm[x] = c - 1
        }
    }

    fun longestCommonPrefix(words: Array<String>): IntArray {
        this.words = words
        n = words.size
        run {
            var i = 0
            while (i + 1 < n) {
                add(i, i + 1)
                i = i + 1
            }
        }
        var ans = IntArray(n)
        for (i in 0 until n) {
            remove(i, i + 1)
            remove(i - 1, i)
            add(i - 1, i + 1)
            if (!tm.isEmpty() && tm.lastKey() > 0) ans[i] = tm.lastKey()
            remove(i - 1, i + 1)
            add(i - 1, i)
            add(i, i + 1)
        }
        return ans
    }
}
