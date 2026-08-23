// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] maximumLength(int[] nums) {
        int n = nums.length;
        int[] left = new int[n], right = new int[n];
        List<Integer> st = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && nums[st.get(st.size() - 1)] < nums[i]) st.remove(st.size() - 1);
            left[i] = st.isEmpty() ? -1 : st.get(st.size() - 1);
            st.add(i);
        }
        st.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!st.isEmpty() && nums[st.get(st.size() - 1)] <= nums[i]) st.remove(st.size() - 1);
            right[i] = st.isEmpty() ? n : st.get(st.size() - 1);
            st.add(i);
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = right[i] - left[i] - 1;
        return ans;
    }
}
