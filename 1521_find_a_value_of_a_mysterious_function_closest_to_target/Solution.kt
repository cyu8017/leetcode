// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

import kotlin.math.abs

class Solution {
    fun closestToTarget(arr: IntArray, target: Int): Int {
        var answer = Int.MAX_VALUE
        var current = HashSet<Int>()
        for (value in arr) {
            val next = HashSet<Int>()
            next.add(value)
            for (previous in current) {
                next.add(value and previous)
            }
            current = next
            for (candidate in current) {
                answer = minOf(answer, abs(candidate - target))
            }
        }
        return answer
    }
}
