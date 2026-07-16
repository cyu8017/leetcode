// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

import java.util.PriorityQueue

class MedianFinder {
    private val small = PriorityQueue<Int>(compareByDescending { it })
    private val large = PriorityQueue<Int>()

    fun addNum(num: Int) {
        small.offer(num)
        large.offer(small.poll())
        if (large.size > small.size) {
            small.offer(large.poll())
        }
    }

    fun findMedian(): Double {
        if (small.size > large.size) {
            return small.peek().toDouble()
        }
        return (small.peek() + large.peek()) / 2.0
    }
}
