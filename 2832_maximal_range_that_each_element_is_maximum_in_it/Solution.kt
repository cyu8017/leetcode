// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

class Solution {
    fun maximumLength(nums: IntArray): IntArray {
        var n = nums.size
        var left = IntArray(n)
        var right = IntArray(n)
        var st = ArrayList<Int>()
        for (i in 0 until n) {
            while (st.isNotEmpty() && nums[st[st.size - 1]] < nums[i]) st.removeAt(st.size - 1)
            left[i] = if (st.isEmpty()) -1 else st[st.size - 1]
            st.add(i)
        }
        st.clear()
        for (i in n - 1 downTo 0) {
            while (st.isNotEmpty() && nums[st[st.size - 1]] <= nums[i]) st.removeAt(st.size - 1)
            right[i] = if (st.isEmpty()) n else st[st.size - 1]
            st.add(i)
        }
        var ans = IntArray(n)
        for (i in 0 until n) { ans[i] = right[i] - left[i] - 1 }
        return ans
    }
}
