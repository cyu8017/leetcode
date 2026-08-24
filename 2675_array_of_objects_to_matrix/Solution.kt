// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

class Solution {
    fun jsonToMatrix(arr: List<java.util.TreeMap<String, String>>): MutableList<MutableList<String>> {
        val keys = java.util.TreeSet<String>()
        for (obj in arr) keys.addAll(obj.keys)
        val mat = ArrayList<MutableList<String>>()
        mat.add(ArrayList(keys))
        for (obj in arr) {
            val row = ArrayList<String>()
            for (k in keys) row.add(obj.getOrDefault(k, ""))
            mat.add(row)
        }
        return mat
    }
}
