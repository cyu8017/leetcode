// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete_prime_number/

class Solution {
    private fun isPrime(x: Int): Boolean {
        if (x < 2) return false
        var i = 2
        while (i * i <= x) {
            if (x % i == 0) return false
            i++
        }
        return true
    }

    fun completePrime(num: Int): Boolean {
        val s = num.toString()
        var x = 0
        for (c in s) {
            x = x * 10 + (c - '0')
            if (!isPrime(x)) return false
        }
        x = 0
        var p = 1
        for (i in s.length - 1 downTo 0) {
            x = p * (s[i] - '0') + x
            p *= 10
            if (!isPrime(x)) return false
        }
        return true
    }
}
