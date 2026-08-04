// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

class Solution {
    fun simplifiedFractions(n: Int): List<String> {
        val answer = mutableListOf<String>()
        for (a in 1 until n) {
            for (b in a + 1..n) {
                if (gcd(a, b) == 1) answer.add("$a/$b")
            }
        }
        return answer
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }
}
