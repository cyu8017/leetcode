// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

import java.util.PriorityQueue

class Solution {
    fun getNumberOfBacklogOrders(orders: Array<IntArray>): Int {
        val mod = 1_000_000_007
        val buy = PriorityQueue<IntArray>(compareByDescending { it[0] })
        val sell = PriorityQueue<IntArray>(compareBy { it[0] })

        for (order in orders) {
            val price = order[0]
            val amount = order[1]
            val orderType = order[2]
            if (orderType == 0) {
                buy.offer(intArrayOf(price, amount))
            } else {
                sell.offer(intArrayOf(price, amount))
            }

            while (buy.isNotEmpty() && sell.isNotEmpty() && buy.peek()[0] >= sell.peek()[0]) {
                val b = buy.poll()
                val s = sell.poll()
                val matched = minOf(b[1], s[1])
                b[1] -= matched
                s[1] -= matched
                if (b[1] > 0) buy.offer(b)
                if (s[1] > 0) sell.offer(s)
            }
        }

        var total = 0
        for (order in buy) total = (total + order[1]) % mod
        for (order in sell) total = (total + order[1]) % mod
        return total
    }
}
