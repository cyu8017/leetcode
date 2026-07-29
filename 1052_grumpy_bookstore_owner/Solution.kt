// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution {
    fun maxSatisfied(customers: IntArray, grumpy: IntArray, minutes: Int): Int {
        var base = 0
        for (i in customers.indices) {
            if (grumpy[i] == 0) base += customers[i]
        }
        var gain = 0
        var best = 0
        for (i in customers.indices) {
            if (grumpy[i] == 1) gain += customers[i]
            if (i >= minutes && grumpy[i - minutes] == 1) {
                gain -= customers[i - minutes]
            }
            best = maxOf(best, gain)
        }
        return base + best
    }
}
