// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution {

    fun maximumCandies(candies: IntArray, k: Long): Int {

            var mx = 0
            for (c in candies) mx = maxOf(mx, c)
            var lo = 0; var hi = mx
            while (lo < hi) {
                var mid = (lo + hi + 1) / 2
                if (can(candies, k, mid)) lo = mid
                else hi = mid - 1
            }
            return lo

    }


    private fun can(candies: IntArray, k: Long, mid: Int): Boolean {

            if (mid == 0) return true
            var cnt = 0
            for (c in candies) {
                cnt += c / mid
                if (cnt >= k) return true
            }
            return false

    }

}
