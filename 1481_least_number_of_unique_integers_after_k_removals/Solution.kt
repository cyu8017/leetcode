// LeetCode 1481 - Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution {
    fun findLeastNumOfUniqueInts(arr: IntArray, k: Int): Int {
        val freq = HashMap<Int, Int>()
        for (x in arr) freq[x] = freq.getOrDefault(x, 0) + 1
        val counts = freq.values.sorted()
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
