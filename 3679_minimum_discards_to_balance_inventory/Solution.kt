// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

class Solution {
    fun minArrivalsToDiscard(arrivals: IntArray, w: Int, m: Int): Int {
        var cnt = HashMap<Int, Int>()
        var n = arrivals.size
        var marked = IntArray(n)
        var ans = 0
        for (i in 0 until n) {
            var x = arrivals[i]
            if (i >= w) cnt.merge(arrivals[i - w], -marked[i - w], { a, b -> a + b })
            if (cnt.getOrDefault(x, 0) >= m) ans++
            else {
                marked[i] = 1
                cnt.merge(x, 1, { a, b -> a + b })
            }
        }
        return ans
    }
}
