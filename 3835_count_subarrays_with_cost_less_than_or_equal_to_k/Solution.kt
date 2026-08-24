// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

class Solution {
    fun countSubarrays(nums: IntArray, k: Long): Long {
        var ans = 0
        var q1 = ArrayDeque<Int>()
        var q2 = ArrayDeque<Int>()
        var l = 0
        for (r in 0 until nums.size) {
            var x = nums[r]
            while (!q1.isEmpty() && nums[q1.peekLast()] <= x) q1.pollLast()
            while (!q2.isEmpty() && nums[q2.peekLast()] >= x) q2.pollLast()
            q1.addLast(r)
            q2.addLast(r)
            while (l < r && (nums[q1.peekFirst()] - nums[q2.peekFirst()]) * (r - l + 1) > k) {
                l++
                if (q1.peekFirst() < l) q1.pollFirst()
                if (q2.peekFirst() < l) q2.pollFirst()
            }
            ans += r - l + 1
        }
        return ans
    }
}
