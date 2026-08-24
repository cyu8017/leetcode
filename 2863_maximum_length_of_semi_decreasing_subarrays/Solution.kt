// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

class Solution {
    fun maxSubarrayLength(nums: IntArray): Int {
        var n = nums.size
        var ans = 0
        var st = ArrayList<Int>()
        for (i in n - 1 downTo 0) {
            if (st.isEmpty() || nums[i] > nums[st[st.size - 1]]) st.add(i)
        }
        for (i in 0 until n) {
            while (st.isNotEmpty() && nums[i] > nums[st[st.size - 1]]) {
                var j = st.removeAt(st.size - 1)
                if (j - i + 1 > ans) ans = j - i + 1
            }
        }
        return ans
    }
}
