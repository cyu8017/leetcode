// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int maxSubarrayLength(int[] nums) {
        int n = nums.length, ans = 0;
        List<Integer> st = new ArrayList<>();
        for (int i = n - 1; i >= 0; i--) {
            if (st.isEmpty() || nums[i] > nums[st.get(st.size() - 1)]) st.add(i);
        }
        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && nums[i] > nums[st.get(st.size() - 1)]) {
                int j = st.remove(st.size() - 1);
                if (j - i + 1 > ans) ans = j - i + 1;
            }
        }
        return ans;
    }
}
