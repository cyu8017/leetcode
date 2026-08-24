// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/


class Solution {
    fun smallestRange(nums: List<List<Int>>): IntArray {
        data class Node(val value: Int, val row: Int, val idx: Int)
        val pq = java.util.PriorityQueue<Node>(compareBy { it.value })
        var maxVal = Int.MIN_VALUE
        for (i in nums.indices) {
            pq.add(Node(nums[i][0], i, 0))
            maxVal = maxOf(maxVal, nums[i][0])
        }
        var bestL = 0
        var bestR = Int.MAX_VALUE
        while (true) {
            val cur = pq.poll()
            if (maxVal - cur.value < bestR - bestL) {
                bestL = cur.value
                bestR = maxVal
            }
            if (cur.idx + 1 == nums[cur.row].size) break
            val nextVal = nums[cur.row][cur.idx + 1]
            pq.add(Node(nextVal, cur.row, cur.idx + 1))
            maxVal = maxOf(maxVal, nextVal)
        }
        return intArrayOf(bestL, bestR)
    }
}
