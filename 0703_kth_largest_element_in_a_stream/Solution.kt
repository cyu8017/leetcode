// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

import java.util.PriorityQueue

class KthLargest(private val k: Int, nums: IntArray) {
    private val heap = PriorityQueue<Int>()

    init {
        for (num in nums) add(num)
    }

    fun add(`val`: Int): Int {
        heap.offer(`val`)
        if (heap.size > k) heap.poll()
        return heap.peek()
    }
}
