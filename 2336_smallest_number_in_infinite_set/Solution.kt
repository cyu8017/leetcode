// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

import java.util.PriorityQueue

class SmallestInfiniteSet {
    private var next = 1
    private val added = HashSet<Int>()
    private val heap = PriorityQueue<Int>()

    fun popSmallest(): Int {
        if (heap.isNotEmpty()) {
            val x = heap.poll()
            added.remove(x)
            return x
        }
        return next++
    }

    fun addBack(num: Int) {
        if (num < next && added.add(num)) {
            heap.offer(num)
        }
    }
}
