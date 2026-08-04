// LeetCode 1304 - Find N Unique Integers Sum up to Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution {
    fun sumZero(n: Int): IntArray {
        val answer = mutableListOf<Int>()
        for (value in 1..n / 2) {
            answer.add(-value)
            answer.add(value)
        }
        if (n % 2 != 0) answer.add(0)
        return answer.toIntArray()
    }
}
