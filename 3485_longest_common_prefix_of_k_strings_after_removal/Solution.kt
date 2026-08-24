// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

class Solution {
    private fun lcpOf(a: MutableList<String>): Int {
        if (a.isEmpty()) return 0
        var pref = a[0]
        for (t in 1 until a.size) {
            var s = a[t]
            var i = 0
            while (i < pref.length && i < s.length && pref[i] == s[i]) i++
            pref = pref.substring(0, i)
            if (pref.isEmpty()) return 0
        }
        return pref.length
    }

    fun longestCommonPrefix(words: Array<String>, k: Int): IntArray {
        var n = words.size
        var ans = IntArray(n)
        for (i in 0 until n) {
            var rest = ArrayList<String>()
            for (j in 0 until n) { if (j != i) rest.add(words[j]) }
            if (rest.size < k) { ans[i] = 0; continue; }
            rest.sort()
            var best = 0
            var j = 0
            while (j + k - 1 < rest.size) {
                var window = rest.subList(j, j + k)
                best = maxOf(best, lcpOf(window))
                j = j + 1
            }
            ans[i] = best
        }
        return ans
    }
}
