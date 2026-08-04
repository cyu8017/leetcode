// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

class Solution {
    fun countVowelPermutation(n: Int): Int {
        val MOD = 1_000_000_007L
        var a = 1L
        var e = 1L
        var i = 1L
        var o = 1L
        var u = 1L
        repeat(n - 1) {
            val na = (e + i + u) % MOD
            val ne = (a + i) % MOD
            val ni = (e + o) % MOD
            val no = i
            val nu = (i + o) % MOD
            a = na; e = ne; i = ni; o = no; u = nu
        }
        return ((a + e + i + o + u) % MOD).toInt()
    }
}
