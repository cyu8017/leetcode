// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

class Solution {
    fun countLargestGroup(n: Int): Int {
        val counts = HashMap<Int, Int>()
        for (x in 1..n) {
            var sum = 0
            var v = x
            while (v > 0) {
                sum += v % 10
                v /= 10
            }
            counts[sum] = counts.getOrDefault(sum, 0) + 1
        }
        val max = counts.values.maxOrNull() ?: 0
        return counts.values.count { it == max }
    }
}
