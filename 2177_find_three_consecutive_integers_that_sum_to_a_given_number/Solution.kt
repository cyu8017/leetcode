// LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution {
    fun sumOfThree(num: Long): LongArray {
        if (num % 3L != 0L) return longArrayOf()
        val x = num / 3L
        return longArrayOf(x - 1, x, x + 1)
    }
}
