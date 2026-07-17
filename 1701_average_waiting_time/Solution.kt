// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

class Solution {
    fun averageWaitingTime(customers: Array<IntArray>): Double {
        var current = 0L
        var total = 0L
        for (customer in customers) {
            current = maxOf(current, customer[0].toLong()) + customer[1]
            total += current - customer[0]
        }
        return total.toDouble() / customers.size
    }
}
