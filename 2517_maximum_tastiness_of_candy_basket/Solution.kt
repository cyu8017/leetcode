// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution {
    fun maximumTastiness(price: IntArray, k: Int): Int {
        price.sort()
        fun ok(d: Int): Boolean {
            var cnt = 1
            var last = price[0]
            for (i in 1 until price.size) {
                if (price[i] - last >= d) {
                    cnt++
                    last = price[i]
                    if (cnt >= k) return true
                }
            }
            return false
        }
        var lo = 0
        var hi = price[price.size - 1] - price[0]
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            if (ok(mid)) lo = mid else hi = mid - 1
        }
        return lo
    }
}
