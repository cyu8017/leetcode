// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

class Solution {
    fun maximumLength(s: String): Int {
        val groups = Array(26) { ArrayList<Int>() }
        val n = s.length
        var i = 0
        while (i < n) {
            var j = i
            while (j < n && s[j] == s[i]) j++
            groups[s[i] - 'a'].add(j - i)
            i = j
        }
        var ans = -1
        for (c in 0 until 26) {
            val arr = groups[c]
            if (arr.isEmpty()) continue
            arr.sortDescending()
            for (L in arr[0] downTo 1) {
                var cnt = 0
                for (g in arr) if (g >= L) cnt += g - L + 1
                if (cnt >= 3) { if (L > ans) ans = L; break }
            }
        }
        return ans
    }
}
