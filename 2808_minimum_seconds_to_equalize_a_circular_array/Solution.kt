// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

class Solution {
    fun minimumSeconds(nums: MutableList<Int>): Int {
        val n = nums.size
        val pos = HashMap<Int, ArrayList<Int>>()
        for (i in 0 until n) {
            pos.getOrPut(nums[i]) { ArrayList() }.add(i)
        }
        var ans = n
        for (p in pos.values) {
            var maxGap = 0
            for (i in p.indices) {
                val gap = if (i + 1 < p.size) p[i + 1] - p[i] else p[0] + n - p[i]
                maxGap = maxOf(maxGap, gap / 2)
            }
            ans = minOf(ans, maxGap)
        }
        return ans
    }
}
