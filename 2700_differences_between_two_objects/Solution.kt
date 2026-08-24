// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

class Solution {
    fun objDiff(
        obj1: java.util.TreeMap<String, Int>,
        obj2: java.util.TreeMap<String, Int>
    ): java.util.TreeMap<String, IntArray> {
        val diff = java.util.TreeMap<String, IntArray>()
        for ((k, v1) in obj1) {
            val v2 = obj2[k]
            if (v2 != null && v2 != v1) diff[k] = intArrayOf(v1, v2)
        }
        return diff
    }
}
