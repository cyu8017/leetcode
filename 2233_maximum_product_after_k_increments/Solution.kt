// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

class Solution {

    fun maximumProduct(nums: IntArray, k: Int): Int {

            var MOD = 1_000_000_007
            var h = PriorityQueue()
            for (x in nums) h.offer(x)
            for (i in 0 until k) {
                var x = h.poll()
                h.offer(x + 1)
            }
            var ans = 1
            while (!h.isEmpty()) {
                ans = ans * h.poll() % MOD
            }
            return ans.toInt()

    }

}
