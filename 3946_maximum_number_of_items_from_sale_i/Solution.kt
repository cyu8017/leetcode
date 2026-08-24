// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

class Solution {
    fun maximumSaleItems(items: Array<IntArray>, budget: Int): Int {
        val f = IntArray(budget + 1)
        var mn = Int.MAX_VALUE
        for (item in items) {
            val factor = item[0]
            val price = item[1]
            mn = minOf(mn, price)
            var cnt = 0
            for (jItem in items) {
                if (jItem[0] % factor == 0) cnt++
            }
            for (j in budget downTo price) {
                f[j] = maxOf(f[j], f[j - price] + cnt)
            }
        }
        var ans = 0
        for (i in 0..budget) {
            val extra = (budget - i) / mn
            ans = maxOf(ans, f[i] + extra)
        }
        return ans
    }
}
