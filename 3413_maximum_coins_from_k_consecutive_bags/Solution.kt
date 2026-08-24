// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

class Solution {
    fun maximumCoins(coins: Array<IntArray>, k: Int): Long {
        coins.sortBy { it[0] }
        var ans = 0L
        val n = coins.size
        for (i in 0 until n) {
            var sum = 0L
            val start = coins[i][0]
            val end = start + k - 1
            var j = i
            while (j < n && coins[j][0] <= end) {
                var l = coins[j][0]
                var r = coins[j][1]
                if (r > end) r = end
                if (l < start) l = start
                if (l <= r) sum += (r - l + 1).toLong() * coins[j][2]
                j++
            }
            if (sum > ans) ans = sum
        }
        for (i in 0 until n) {
            var sum = 0L
            val end = coins[i][1]
            val start = end - k + 1
            for (j in 0..i) {
                var l = coins[j][0]
                var r = coins[j][1]
                if (l < start) l = start
                if (r > end) r = end
                if (l <= r) sum += (r - l + 1).toLong() * coins[j][2]
            }
            if (sum > ans) ans = sum
        }
        return ans
    }
}
