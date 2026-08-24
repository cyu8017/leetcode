// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution {
    fun smallestNumber(pattern: String): String {
        val n = pattern.length
        val ans = CharArray(n + 1) { i -> ('1' + i) }
        var i = 0
        while (i < n) {
            if (pattern[i] == 'I') {
                i++
                continue
            }
            var j = i
            while (j < n && pattern[j] == 'D') j++
            reverse(ans, i, j)
            i = j
        }
        return String(ans)
    }

    private fun reverse(a: CharArray, l0: Int, r0: Int) {
        var l = l0
        var r = r0
        while (l < r) {
            val t = a[l]
            a[l] = a[r]
            a[r] = t
            l++
            r--
        }
    }
}
