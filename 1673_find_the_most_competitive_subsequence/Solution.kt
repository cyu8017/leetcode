// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution {
    fun mostCompetitive(nums: IntArray, k: Int): IntArray {
        val st = ArrayDeque<Int>()
        for (i in nums.indices) {
            val x = nums[i]
            while (st.isNotEmpty() && st.last() > x && st.size - 1 + nums.size - i >= k) {
                st.removeLast()
            }
            if (st.size < k) st.addLast(x)
        }
        return st.toIntArray()
    }
}
