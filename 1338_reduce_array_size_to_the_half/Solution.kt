// LeetCode 1338 - Reduce Array Size to The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution {
    fun minSetSize(arr: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (v in arr) freq[v] = freq.getOrDefault(v, 0) + 1
        val counts = freq.values.sortedDescending()
        var removed = 0
        for ((i, c) in counts.withIndex()) {
            removed += c
            if (removed * 2 >= arr.size) return i + 1
        }
        return 0
    }
}
