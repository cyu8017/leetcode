// LeetCode 1925
// https://leetcode.com/problems/count-square-sum-triples/

class Solution {
    fun countTriples(n: Int): Int {
        val squares = (1..n).map { it * it }.toHashSet()
        var ans = 0
        for (a in 1..n) for (b in 1..n) if (a * a + b * b in squares) ans++
        return ans
    }
}
