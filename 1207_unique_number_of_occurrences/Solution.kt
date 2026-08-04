// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

class Solution {
    fun uniqueOccurrences(arr: IntArray): Boolean {
        val count = mutableMapOf<Int, Int>()
        for (x in arr) count[x] = count.getOrDefault(x, 0) + 1
        val seen = mutableSetOf<Int>()
        for (c in count.values) if (!seen.add(c)) return false
        return true
    }
}
