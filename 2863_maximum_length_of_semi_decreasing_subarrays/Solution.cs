// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

using System.Collections.Generic;

public class Solution {
    public int MaxSubarrayLength(int[] nums) {
        int n = nums.Length, ans = 0;
        var st = new List<int>();
        for (int i = n - 1; i >= 0; i--) {
            if (st.Count == 0 || nums[i] > nums[st[st.Count - 1]]) st.Add(i);
        }
        for (int i = 0; i < n; i++) {
            while (st.Count > 0 && nums[i] > nums[st[st.Count - 1]]) {
                int j = st[st.Count - 1];
                st.RemoveAt(st.Count - 1);
                if (j - i + 1 > ans) ans = j - i + 1;
            }
        }
        return ans;
    }
}
