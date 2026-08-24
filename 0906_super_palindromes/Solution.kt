// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

class Solution {
    fun superpalindromesInRange(left: String, right: String): Int {
        val L = left.toLong()
        val R = right.toLong()
        var ans = 0
        for (k in 1L..100000L) {
            val s = k.toString()
            val rev = s.reversed()
            val pal = (s + rev).toLong()
            val sq = pal * pal
            if (sq > R) break
            if (sq >= L && isPal(sq)) ans++
        }
        for (k in 1L..100000L) {
            val s = k.toString()
            val rev = s.substring(0, s.length - 1).reversed()
            val pal = (s + rev).toLong()
            val sq = pal * pal
            if (sq > R) break
            if (sq >= L && isPal(sq)) ans++
        }
        return ans
    }

    private fun isPal(x: Long): Boolean {
        val s = x.toString()
        val n = s.length
        for (i in 0 until n / 2) if (s[i] != s[n - 1 - i]) return false
        return true
    }
}
