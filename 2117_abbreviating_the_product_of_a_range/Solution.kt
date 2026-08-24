// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

class Solution {
    fun abbreviateProduct(left: Int, right: Int): String {
        var twos: Int = 0, fives = 0
        for (i in left until = right) {
            var x: Int = i
            while (x % 2 == 0) { twos++; x /= 2; }
            while (x % 5 == 0) { fives++; x /= 5; }
        }
        var zeros: Int = minOf(twos, fives)
        long MOD = 100000000000L
        var prod: Long = 1
        var extra2: Int = twos - zeros, extra5 = fives - zeros
        var logSum: Double = 0.0
        for (i in left until = right) {
            var x: Int = i
            while (x % 2 == 0) x /= 2
            while (x % 5 == 0) x /= 5
            prod = (prod * x) % MOD
            logSum += Math.log10(x)
        }
        for (i in 0 until extra2) { prod = (prod * 2) % MOD; logSum += Math.log10(2.0); }
        for (i in 0 until extra5) { prod = (prod * 5) % MOD; logSum += Math.log10(5.0); }
        var fullLog: Double = 0.0
        for (i in left until = right) fullLog += Math.log10(i)
        var digits: Int = fullLog + 1
        if (digits <= 10) {
            var p: Long = 1
            for (i in left until = right) p *= i
            return Long.toString(p)
        }
        var frac: Double = logSum - Math.floor(logSum)
        var prefix: Long = Math.pow(10.0, frac + 4)
        var suffix: Long = prod % 100000
        return prefix + "e" + zeros + String.format("%05d", suffix)
    }
}
