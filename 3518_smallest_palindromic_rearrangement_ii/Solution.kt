// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

class Solution {
    val MAX = 1000001

    fun nCk(n: Int, kk0: Int): Int {
        var kk = kk0
        if (kk < 0 || kk > n) return 0
        var res = 1L
        if (kk > n - kk) kk = n - kk
        for (i in 1..kk) {
            res = res * (n - i + 1) / i
            if (res >= MAX) return MAX
        }
        return res.toInt()
    }

    fun countArr(h: IntArray): Int {
        var total = 0
        for (f in h) total += f
        var res = 1L
        for (f in h) {
            res *= nCk(total, f).toLong()
            if (res >= MAX) return MAX
            total -= f
        }
        return res.toInt()
    }

    fun smallestPalindrome(s: String, k0: Int): String {
        var k = k0
        val cnt = IntArray(26)
        for (c in s) cnt[c - 'a']++
        var odd = 0
        for (c in cnt) if (c % 2 != 0) odd++
        if (odd > 1) return ""
        val half = IntArray(26)
        var mid = '\u0000'
        for (i in 0 until 26) {
            half[i] = cnt[i] / 2
            if (cnt[i] % 2 != 0) mid = ('a'.code + i).toChar()
        }
        if (countArr(half) < k) return ""
        var halfLen = 0
        for (f in half) halfLen += f
        val left = StringBuilder()
        for (t in 0 until halfLen) {
            for (i in 0 until 26) {
                if (half[i] == 0) continue
                half[i]--
                val arr = countArr(half)
                if (arr >= k) {
                    left.append(('a'.code + i).toChar())
                    break
                }
                k -= arr
                half[i]++
            }
        }
        val res = StringBuilder()
        res.append(left)
        if (mid != '\u0000') res.append(mid)
        for (i in left.length - 1 downTo 0) res.append(left[i])
        return res.toString()
    }
}
