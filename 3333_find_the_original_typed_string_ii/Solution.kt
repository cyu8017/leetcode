// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

class Solution {
    fun possibleStringCount(word: String, k: Int): Int {
        val mod = 1000000007
        var groups = ArrayList<Int>()
        var i = 0
        while (i < word.length) {
            var j = i
            while (j < word.length && word[j] == word[i]) j++
            groups.add(j - i)
            i = j
            
        }
        var total = 1
        for (g in groups) { total = (total * g % mod) }
        if (k <= groups.size) return total
        var need = k - 1
        var dp = IntArray(need)
        dp[0] = 1
        for (g in groups) {
            var ndp = IntArray(need)
            var pref = IntArray(need + 1)
            for (i in 0 until need) { pref[i + 1] = (pref[i] + dp[i]) % mod }
            for (s in 0 until need) {
                var lo = s - g
                if (lo < 0) lo = 0
                var hi = s - 1
                if (hi >= 0) ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod
            }
            dp = ndp
        }
        var bad = 0
        for (v in dp) { bad = (bad + v) % mod }
        return (total - bad + mod) % mod
    }
}
