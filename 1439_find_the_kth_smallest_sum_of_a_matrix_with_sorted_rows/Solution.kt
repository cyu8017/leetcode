// LeetCode 1439 - Find the Kth Smallest Sum of a Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

import java.util.PriorityQueue

class Solution {
    fun kthSmallest(mat: Array<IntArray>, k: Int): Int {
        var sums = mutableListOf(0)
        for (row in mat) {
            val heap = PriorityQueue<IntArray>(compareBy { it[0] })
            heap.offer(intArrayOf(sums[0] + row[0], 0, 0))
            val merged = mutableListOf<Int>()
            while (heap.isNotEmpty() && merged.size < k) {
                val cur = heap.poll()
                val value = cur[0]
                val i = cur[1]
                val j = cur[2]
                merged.add(value)
                if (j + 1 < row.size) {
                    heap.offer(intArrayOf(sums[i] + row[j + 1], i, j + 1))
                }
                if (j == 0 && i + 1 < sums.size) {
                    heap.offer(intArrayOf(sums[i + 1] + row[0], i + 1, 0))
                }
            }
            sums = merged
        }
        return sums[k - 1]
    }
}
