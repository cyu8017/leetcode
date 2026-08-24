// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

class Solution {
    fun minOperations(nums: IntArray): Int {
        var st = HashSet<Int>()
        for (i in nums.size - 1 downTo 0) {
            if (st.contains(nums[i])) return i / 3 + 1
            st.add(nums[i])
        }
        return 0
    }
}
