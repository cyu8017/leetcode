// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

class Solution {
    fun maxProduct(s: String): Int {
        val n = s.length
        var best = 0
        val total = 1 shl n
        for (mask1 in 1 until total) {
            val len1 = palLen(s, mask1)
            if (len1 == 0) continue
            val remain = (total - 1) xor mask1
            var mask2 = remain
            while (mask2 > 0) {
                val len2 = palLen(s, mask2)
                if (len2 > 0 && len1 * len2 > best) best = len1 * len2
                mask2 = (mask2 - 1) and remain
            }
        }
        return best
    }

    private fun palLen(s: String, mask: Int): Int {
        val chars = StringBuilder()
        for (i in 0 until s.length) {
            if ((mask and (1 shl i)) != 0) chars.append(s[i])
        }
        var l = 0
        var r = chars.length - 1
        while (l < r) {
            if (chars[l] != chars[r]) return 0
            l++
            r--
        }
        return chars.length
    }
}
