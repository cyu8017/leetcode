// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

class Solution {
    fun relativeSortArray(arr1: IntArray, arr2: IntArray): IntArray {
        val count = mutableMapOf<Int, Int>()
        for (x in arr1) count[x] = count.getOrDefault(x, 0) + 1
        val ans = mutableListOf<Int>()
        for (x in arr2) {
            repeat(count.remove(x) ?: 0) { ans.add(x) }
        }
        for (x in count.keys.sorted()) {
            repeat(count[x]!!) { ans.add(x) }
        }
        return ans.toIntArray()
    }
}
