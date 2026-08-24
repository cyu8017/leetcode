// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

class Solution {
    fun maximumSumOfHeights(maxHeights: List<Int>): Long {
        val n = maxHeights.size
        val left = LongArray(n)
        var st = ArrayList<Int>()
        st.add(-1)
        var sum = 0L
        for (i in 0 until n) {
            while (st.size > 1 && maxHeights[st[st.size - 1]] >= maxHeights[i]) {
                val j = st.removeAt(st.size - 1)
                sum -= 1L * maxHeights[j] * (j - st[st.size - 1])
            }
            sum += 1L * maxHeights[i] * (i - st[st.size - 1])
            left[i] = sum
            st.add(i)
        }
        val right = LongArray(n)
        st = ArrayList()
        st.add(n)
        sum = 0L
        for (i in n - 1 downTo 0) {
            while (st.size > 1 && maxHeights[st[st.size - 1]] >= maxHeights[i]) {
                val j = st.removeAt(st.size - 1)
                sum -= 1L * maxHeights[j] * (st[st.size - 1] - j)
            }
            sum += 1L * maxHeights[i] * (st[st.size - 1] - i)
            right[i] = sum
            st.add(i)
        }
        var ans = 0L
        for (i in 0 until n) {
            val cand = left[i] + right[i] - maxHeights[i]
            if (cand > ans) ans = cand
        }
        return ans
    }
}
