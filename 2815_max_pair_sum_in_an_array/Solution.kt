// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution {
    fun maxSum(nums: IntArray): Int {
        var best = HashMap<Int, Int>()
        var ans = -1
        for (v in nums) {
            var x = v
            var md = 0
            while (x > 0) { md = maxOf(md, x % 10); x /= 10; }
            if (best.containsKey(md)) {
                ans = maxOf(ans, best[md] + v)
                best[md] = maxOf(best[md], v)
            } else best[md] = v
        }
        return ans
    }
}
