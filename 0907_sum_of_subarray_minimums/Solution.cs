// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

using System.Collections.Generic;

public class Solution {
    public int SumSubarrayMins(int[] arr) {
        const int MOD = 1000000007;
        int n = arr.Length;
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) { left[i] = -1; right[i] = n; }
        var st = new Stack<int>();
        for (int i = 0; i < n; i++) {
            while (st.Count > 0 && arr[st.Peek()] > arr[i]) st.Pop();
            left[i] = st.Count == 0 ? -1 : st.Peek();
            st.Push(i);
        }
        st.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (st.Count > 0 && arr[st.Peek()] >= arr[i]) st.Pop();
            right[i] = st.Count == 0 ? n : st.Peek();
            st.Push(i);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans + (long)arr[i] * (i - left[i]) * (right[i] - i)) % MOD;
        }
        return (int)ans;
    }
}
