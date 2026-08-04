// LeetCode 1979
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution {
    fun findGCD(nums: IntArray): Int {
        fun gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
        return gcd(nums.minOrNull()!!, nums.maxOrNull()!!)
    }
}
