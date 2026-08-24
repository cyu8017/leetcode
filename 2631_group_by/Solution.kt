// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

class Solution {
    fun groupBy(arr: IntArray, fn: (Int) -> String): MutableMap<String, MutableList<Int>> {
        val out = HashMap<String, MutableList<Int>>()
        for (x in arr) {
            val k = fn(x)
            out.getOrPut(k) { ArrayList() }.add(x)
        }
        return out
    }
}
