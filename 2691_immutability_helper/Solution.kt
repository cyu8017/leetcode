// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

class Solution {
    fun immutableHelper(
        obj: java.util.TreeMap<String, Int>,
        mutators: List<(java.util.TreeMap<String, Int>) -> Unit>
    ): MutableList<java.util.TreeMap<String, Int>> {
        val out = ArrayList<java.util.TreeMap<String, Int>>()
        for (m in mutators) {
            val copy = java.util.TreeMap(obj)
            m(copy)
            out.add(copy)
        }
        return out
    }
}
