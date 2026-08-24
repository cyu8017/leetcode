// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

import java.util.PriorityQueue

class Solution {
    fun minBuildTime(blocks: IntArray, split: Int): Int {
        val heap = PriorityQueue<Int>()
        for (b in blocks) heap.offer(b)
        while (heap.size > 1) {
            heap.poll()
            heap.offer(heap.poll() + split)
        }
        return heap.peek()
    }
}
