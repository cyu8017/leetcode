// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution {
    fun minimumCost(cost: IntArray): Int {
        val arr = cost.sortedDescending()
        var ans = 0
        for (i in arr.indices) {
            if (i % 3 != 2) ans += arr[i]
        }
        return ans
    }
}
