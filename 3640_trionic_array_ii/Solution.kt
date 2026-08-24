// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

class Solution {
    fun maxSumTrionic(nums: IntArray): Long {
        var n = nums.size
        var i = 0
        var ans = Long.MIN_VALUE
        while (i < n) {
            var l = i
            for (i++; i < n && nums[i - 1] < nums[i];) i++
            if (i == l + 1) continue
            var p = i - 1
            var s = nums[p - 1] + nums[p]
            while (i < n && nums[i - 1] > nums[i]) {
                s += nums[i]
                i++
            }
            if (i == p + 1 || i == n || nums[i - 1] == nums[i]) continue
            var q = i - 1
            s += nums[i]
            i++
            var mx = 0
            var t = 0
            while (i < n && nums[i - 1] < nums[i]) {
                t += nums[i]
                i++
                mx = maxOf(mx, t)
            }
            s += mx
            mx = t = 0
            for (j in p - 2 downTo l) {
                t += nums[j]
                mx = maxOf(mx, t)
            }
            s += mx
            ans = maxOf(ans, s)
            i = q
        }
        return ans
    }
}
