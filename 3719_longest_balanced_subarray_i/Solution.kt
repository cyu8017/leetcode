// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

class Solution {
    fun longestBalanced(nums: IntArray): Int {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            var vis = HashSet<Int>()
            var cnt = IntArray(2)
            for (j in i until n) {
                if (!vis.contains(nums[j])) {
                    vis.add(nums[j])
                    cnt[nums[j] & 1]++
                }
                if (cnt[0] == cnt[1]) ans = maxOf(ans, j - i + 1)
            }
        }
        return ans
    }
}
