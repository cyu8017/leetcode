// LeetCode 1310 - XOR Queries Of A Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution {
    fun xorQueries(arr: IntArray, queries: Array<IntArray>): IntArray {
        val prefix = IntArray(arr.size + 1)
        for (i in arr.indices) prefix[i + 1] = prefix[i] xor arr[i]
        return IntArray(queries.size) { i ->
            val left = queries[i][0]
            val right = queries[i][1]
            prefix[right + 1] xor prefix[left]
        }
    }
}
