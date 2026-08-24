// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

class Solution {
    fun join(
        arr1: List<java.util.TreeMap<String, Int>>,
        arr2: List<java.util.TreeMap<String, Int>>
    ): MutableList<java.util.TreeMap<String, Int>> {
        val byId = java.util.TreeMap<Int, java.util.TreeMap<String, Int>>()
        merge(byId, arr1)
        merge(byId, arr2)
        return ArrayList(byId.values)
    }

    private fun merge(
        byId: java.util.TreeMap<Int, java.util.TreeMap<String, Int>>,
        arr: List<java.util.TreeMap<String, Int>>
    ) {
        for (obj in arr) {
            val id = obj["id"]!!
            val dest = byId.getOrPut(id) { java.util.TreeMap() }
            dest.putAll(obj)
        }
    }
}
