// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

class Solution {
    fun numDupDigitsAtMostN(n: Int): Int {
        val s = n.toString()
        val m = s.length
        var totalUnique = 0
        for (length in 1 until m) totalUnique += 9 * P(9, length - 1)
        val used = BooleanArray(10)
        var broken = false
        for (i in 0 until m) {
            val d = s[i] - '0'
            val start = if (i == 0) 1 else 0
            for (x in start until d) {
                if (used[x]) continue
                totalUnique += P(9 - i, m - i - 1)
            }
            if (used[d]) {
                broken = true
                break
            }
            used[d] = true
        }
        if (!broken) totalUnique++
        return n - totalUnique
    }

    private fun P(a: Int, b: Int): Int {
        var res = 1
        for (i in 0 until b) res *= a - i
        return res
    }
}
