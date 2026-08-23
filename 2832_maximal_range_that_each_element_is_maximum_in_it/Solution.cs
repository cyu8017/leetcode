// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

using System.Collections.Generic;

public class Solution {
    public int[] MaximumLength(int[] nums) {
        int n = nums.Length;
        int[] left = new int[n], right = new int[n];
        var st = new List<int>();
        for (int i = 0; i < n; i++) {
            while (st.Count > 0 && nums[st[st.Count - 1]] < nums[i]) st.RemoveAt(st.Count - 1);
            left[i] = st.Count == 0 ? -1 : st[st.Count - 1];
            st.Add(i);
        }
        st.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (st.Count > 0 && nums[st[st.Count - 1]] <= nums[i]) st.RemoveAt(st.Count - 1);
            right[i] = st.Count == 0 ? n : st[st.Count - 1];
            st.Add(i);
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = right[i] - left[i] - 1;
        return ans;
    }
}
