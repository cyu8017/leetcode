// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

class Solution {
    private fun modPowP(a: Int, e: Int, p: Int): Int {
        var r = 1
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % p
            a = a * a % p
            e >>= 1
        }
        return r
    }
    private fun modInvPrime(a: Int, p: Int): Int { return modPowP(a, p - 2, p) }
    private fun binomMod(n: Int, k: Int, p: Int): Int {
        if (k < 0 || k > n) return 0
        var num = 1
        var den = 1
        for (i in 0 until k) {
            num = num * (n - i) % p
            den = den * (i + 1) % p
        }
        return num * modInvPrime(den, p) % p
    }
    private fun crt(a1: Int, m1: Int, a2: Int, m2: Int): Int {
        for (x in 0 until m1 * m2) {
            if (x % m1 == a1 && x % m2 == a2) return x
        }
        return 0
    }
    private fun binomMod10(n: Int, k: Int): Int {
        return crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5)
    }
    private fun combineDigit(s: String, n: Int, offset: Int): Int {
        var sum = 0
        for (i in 0 .. n - 2) {
            sum = (sum + binomMod10(n - 2, i) * (s[i + offset] - '0')) % 10
        }
        return sum
    }
    fun hasSameDigits(s: String): Boolean {
        var n = s.length
        return combineDigit(s, n, 0) == combineDigit(s, n, 1)
    }
}
