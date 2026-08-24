// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

class Solution {
    fun chunk(arr: IntArray, size: Int): Array<IntArray> {
        val ans = ArrayList<IntArray>()
        var i = 0
        while (i < arr.size) {
            val end = minOf(arr.size, i + size)
            ans.add(arr.copyOfRange(i, end))
            i += size
        }
        return ans.toTypedArray()
    }
}
