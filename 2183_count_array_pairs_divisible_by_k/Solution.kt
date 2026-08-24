// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

class Solution {
    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }

    fun countPairs(nums: IntArray, k: Int): Long {
        val freq = HashMap<Int, Int>()
        var ans = 0L
        for (x in nums) {
            val g1 = gcd(x, k)
            for ((key, value) in freq) if (1L * g1 * key % k == 0L) ans += value
            freq.merge(g1, 1) { a, b -> a + b }
        }
        return ans
    }
}
