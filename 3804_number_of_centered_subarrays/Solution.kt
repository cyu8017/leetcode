// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

class Solution {
    fun centeredSubarrays(nums: IntArray): Int {
        val n = nums.size
        var ans = 0
        for (i in 0 until n) {
            val st = HashSet<Int>()
            var s = 0
            for (j in i until n) {
                s += nums[j]
                st.add(nums[j])
                if (st.contains(s)) ans++
            }
        }
        return ans
    }
}
