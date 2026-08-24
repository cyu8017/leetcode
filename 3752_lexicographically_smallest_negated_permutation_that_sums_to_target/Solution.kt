// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

class Solution {
    fun lexicographicallySmallest(n: Int, target: Long): IntArray {
        var total = 1L * n * (n + 1) / 2
        if (target < -total || target > total || (total - target) % 2 != 0) return IntArray(0)
        var remaining = (total - target) / 2
        var negative = BooleanArray(n + 1)
        for (value in n downTo 1) {
            if (value <= remaining) {
                negative[value] = true
                remaining -= value
            }
        }
        var answer = ArrayList<Int>()
        for (value in n downTo 1) {
            if (negative[value]) answer.add(-value)
        }
        for (value in 1 ..n) {
            if (!negative[value]) answer.add(value)
        }
        return answer.toIntArray()
    }
}
