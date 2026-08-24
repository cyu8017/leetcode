// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

class Solution {
    fun maxPrice(items: Array<IntArray>, capacity: Int): Double {
        items.sortWith(compareByDescending { it[0].toDouble() / it[1] })
        var ans = 0.0
        var remain = capacity
        for (it in items) {
            val price = it[0]
            val weight = it[1]
            if (remain >= weight) {
                ans += price
                remain -= weight
            } else {
                ans += price.toDouble() * remain / weight
                remain = 0
                break
            }
        }
        return if (remain > 0) -1.0 else ans
    }
}
