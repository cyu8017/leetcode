// LeetCode 1331 - Rank Transform of an Array
// https://leetcode.com/problems/rank-transform-of-an-array/

class Solution {
    fun arrayRankTransform(arr: IntArray): IntArray {
        val sorted = arr.toSet().sorted()
        val rank = HashMap<Int, Int>()
        for (i in sorted.indices) {
            rank[sorted[i]] = i + 1
        }
        return IntArray(arr.size) { rank[arr[it]]!! }
    }
}
