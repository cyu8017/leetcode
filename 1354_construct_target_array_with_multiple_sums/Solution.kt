// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

import java.util.PriorityQueue

class Solution {
    fun isPossible(target: IntArray): Boolean {
        if (target.size == 1) return target[0] == 1
        var total = 0L
        val pq = PriorityQueue<Long>(compareByDescending { it })
        for (x in target) {
            total += x
            pq.offer(x.toLong())
        }
        while (true) {
            val x = pq.poll()
            val rest = total - x
            if (x == 1L || rest == 1L) return true
            if (rest == 0L || x <= rest) return false
            val prev = x % rest
            if (prev == 0L) return false
            total = rest + prev
            pq.offer(prev)
        }
    }
}
