// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

class Solution {
    fun simplifiedFractions(n: Int): List<String> {
        fun gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
        val answer = mutableListOf<String>()
        for (a in 1 until n) {
            for (b in a + 1..n) {
                if (gcd(a, b) == 1) answer.add("$a/$b")
            }
        }
        return answer
    }
}
