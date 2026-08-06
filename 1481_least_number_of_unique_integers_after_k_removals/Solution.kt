// LeetCode 1481 - Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution {
    fun findLeastNumOfUniqueInts(arr: IntArray, k: Int): Int {
        val counts = arr.toList().groupingBy { it }.eachCount().values.sorted()
        var remaining = k
        var removed = 0
        for (count in counts) {
            if (remaining < count) break
            remaining -= count
            removed++
        }
        return counts.size - removed
    }
}
