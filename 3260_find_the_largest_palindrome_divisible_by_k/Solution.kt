// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

class Solution {
    fun largestPalindrome(n: Int, k: Int): String {
        val digits = repeat('9', n)
        val half = (n + 1) / 2
        when (k) {
            1, 3, 9 -> return String(digits)
            2 -> {
                digits[0] = '8'
                digits[n - 1] = '8'
                return String(digits)
            }
            4 -> {
                if (n == 1) return "8"
                digits[0] = '8'
                digits[1] = '8'
                digits[n - 1] = '8'
                digits[n - 2] = '8'
                return String(digits)
            }
            5 -> {
                digits[0] = '5'
                digits[n - 1] = '5'
                return String(digits)
            }
            8 -> {
                if (n <= 2) return String(repeat('8', n))
                digits[0] = '8'
                digits[1] = '8'
                digits[2] = '8'
                digits[n - 1] = '8'
                digits[n - 2] = '8'
                digits[n - 3] = '8'
                return String(digits)
            }
            6 -> {
                if (n == 1) return "6"
                digits[0] = '8'
                digits[n - 1] = '8'
                val sum = 16 + 9 * (n - 2)
                val need = sum % 3
                if (need != 0) {
                    val pos = half - 1
                    digits[pos] = ('0'.code + (digits[pos] - '0') - need).toChar()
                    if (n % 2 == 0 || pos != n - 1 - pos) digits[n - 1 - pos] = digits[pos]
                }
                return String(digits)
            }
            7 -> return largestPal7(n)
            else -> return String(digits)
        }
    }

    private fun repeat(c: Char, n: Int): CharArray {
        val a = CharArray(n)
        a.fill(c)
        return a
    }

    private fun mod7(s: String): Int {
        var r = 0
        for (ch in s) r = (r * 10 + (ch - '0')) % 7
        return r
    }

    private fun largestPal7(n: Int): String {
        val halfLen = (n + 1) / 2
        val half = repeat('9', halfLen)
        while (true) {
            val pal = CharArray(n)
            for (i in 0 until halfLen) pal[i] = half[i]
            for (i in 0 until n / 2) pal[n - 1 - i] = pal[i]
            if (mod7(String(pal)) == 0) return String(pal)
            var idx = halfLen - 1
            while (idx >= 0 && half[idx] == '0') {
                half[idx] = '9'
                idx--
            }
            if (idx < 0) break
            half[idx]--
        }
        return ""
    }
}
