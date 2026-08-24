// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum_capacity_within_budget/

import java.util.PriorityQueue

class Solution {
    fun maxCapacity(costs: IntArray, capacity: IntArray, budget: Int): Int {
        val arr = ArrayList<IntArray>()
        for (k in costs.indices) {
            if (costs[k] < budget) arr.add(intArrayOf(costs[k], capacity[k]))
        }
        if (arr.isEmpty()) return 0
        arr.sortBy { it[0] }
        val m = arr.size
        val alive = BooleanArray(m) { true }
        val h = PriorityQueue<IntArray> { a, b ->
            if (a[0] != b[0]) b[0].compareTo(a[0]) else b[1].compareTo(a[1])
        }
        for (i in 0 until m) h.offer(intArrayOf(arr[i][1], i))
        while (h.isNotEmpty() && !alive[h.peek()[1]]) { h.poll() }
        var ans = h.peek()[0]
        var i = 0
        var j = m - 1
        while (i < j) {
            alive[i] = false
            while (i < j && arr[i][0] + arr[j][0] >= budget) {
                alive[j] = false
                j--
            }
            while (h.isNotEmpty() && !alive[h.peek()[1]]) { h.poll() }
            if (h.isNotEmpty()) ans = maxOf(ans, arr[i][1] + h.peek()[0])
            i++
        }
        return ans
    }
}
