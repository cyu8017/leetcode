// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

class Solution {
    fun countBinaryPalindromes(n: Long): Int {
        if (n == 0) return 1
        var ans = 1
        var sb = StringBuilder()
        run {
            var x = n
            while (x > 0) {
                sb.append((char) ('0' + (x & 1)))
                x >>= 1
            }
        }
        var s = sb.reverse().toString()
        var L = s.length
        for (len in 1 until L) {
            var half = (len + 1) / 2
            ans += 1  shl  (half - 1)
        }
        var half = (L + 1) / 2
        var prefix = s.substring(0, half)
        var start = 1  shl  (half - 1)
        var prefVal = 0
        for (c in prefix.toCharArray()) { prefVal = (prefVal  shl  1) | (c - '0') }
        ans += prefVal - start
        var pal = StringBuilder(prefix)
        run {
            var i = half - 1 - (L % 2)
            while (i >= 0) {
                pal.append(prefix[i])
                i--
            }
        }
        var pval = 0
        for (c in pal.toString().toCharArray()) { pval = (pval  shl  1) | (c - '0') }
        if (pval <= n) ans++
        return ans
    }
}
