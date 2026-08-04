// LeetCode 1962
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import java.util.PriorityQueue

class Solution {
    fun minStoneSum(piles: IntArray, k: Int): Int {
        val heap = PriorityQueue<Int>(compareByDescending { it })
        for (p in piles) heap.add(p)
        repeat(k) {
            val x = heap.poll()
            heap.add(x - x / 2)
        }
        return heap.sum()
    }
}
