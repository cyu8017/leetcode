// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

import java.util.*;

class Solution {
    public int sumSubarrayMins(int[] arr) {
        final int MOD = 1_000_000_007;
        int n = arr.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Arrays.fill(left, -1);
        Arrays.fill(right, n);
        Deque<Integer> st = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && arr[st.peek()] > arr[i]) st.pop();
            left[i] = st.isEmpty() ? -1 : st.peek();
            st.push(i);
        }
        st.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!st.isEmpty() && arr[st.peek()] >= arr[i]) st.pop();
            right[i] = st.isEmpty() ? n : st.peek();
            st.push(i);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans + (long) arr[i] * (i - left[i]) * (right[i] - i)) % MOD;
        }
        return (int) ans;
    }
}
