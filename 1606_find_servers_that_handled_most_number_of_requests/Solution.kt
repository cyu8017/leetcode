// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

import java.util.PriorityQueue
import java.util.TreeSet

class Solution {
    fun busiestServers(k: Int, arrival: IntArray, load: IntArray): List<Int> {
        val free = TreeSet<Int>()
        for (i in 0 until k) free.add(i)
        val busy = PriorityQueue(compareBy<IntArray> { it[0] })
        val count = IntArray(k)
        for (i in arrival.indices) {
            val t = arrival[i]
            while (busy.isNotEmpty() && busy.peek()[0] <= t) {
                free.add(busy.poll()[1])
            }
            if (free.isEmpty()) continue
            val prefer = i % k
            val server = free.ceiling(prefer) ?: free.first()
            free.remove(server)
            count[server]++
            busy.offer(intArrayOf(t + load[i], server))
        }
        val best = count.maxOrNull() ?: 0
        return count.indices.filter { count[it] == best }
    }
}
