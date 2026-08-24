// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

class Solution {
    fun recoverOrder(order: IntArray, friends: IntArray): IntArray {
        val n = order.size
        val d = IntArray(n + 1)
        for (i in 0 until n) d[order[i]] = i
        val boxed = friends.toTypedArray()
        boxed.sortBy { d[it] }
        for (i in friends.indices) friends[i] = boxed[i]
        return friends
    }
}
