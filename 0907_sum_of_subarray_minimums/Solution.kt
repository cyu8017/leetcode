// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution {
    fun sumSubarrayMins(arr: IntArray): Int {
        var MOD = 1_000_000_007
        var n = arr.size
        var left = IntArray(n)
        var right = IntArray(n)
        left.fill(-1)
        right.fill(n)
        var st = ArrayDeque()
        for (i in 0 until n) {
            while (!st.isEmpty() && arr[st.first()] > arr[i]) st.pop()
            left[i] = if (st.isEmpty()) -1 else st.first()
            st.push(i)
        }
        st.clear()
        for (i in n - 1 downTo 0) {
            while (!st.isEmpty() && arr[st.first()] >= arr[i]) st.pop()
            right[i] = if (st.isEmpty()) n else st.first()
            st.push(i)
        }
        var ans = 0
        for (i in 0 until n) {
            ans = (ans + arr[i] * (i - left[i]) * (right[i] - i)) % MOD
        }
        return ans
    }
}
