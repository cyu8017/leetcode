// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

class Solution {
    fun longestEqualSubarray(nums: MutableList<Int>, k: Int): Int {
        val pos = HashMap<Int, ArrayList<Int>>()
        for (i in nums.indices) {
            pos.getOrPut(nums[i]) { ArrayList() }.add(i)
        }
        var ans = 0
        for (p in pos.values) {
            var left = 0
            for (right in p.indices) {
                while (p[right] - p[left] - (right - left) > k) left++
                ans = maxOf(ans, right - left + 1)
            }
        }
        return ans
    }
}
