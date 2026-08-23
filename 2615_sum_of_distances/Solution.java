// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        long[] ans = new long[n];
        Map<Integer, List<Integer>> pos = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            pos.computeIfAbsent(nums[i], z -> new ArrayList<>()).add(i);
        }
        for (List<Integer> idxs : pos.values()) {
            int m = idxs.size();
            long[] pref = new long[m + 1];
            for (int i = 0; i < m; ++i) pref[i + 1] = pref[i] + idxs.get(i);
            for (int j = 0; j < m; ++j) {
                int idx = idxs.get(j);
                long left = (long) j * idx - pref[j];
                long right = pref[m] - pref[j + 1] - (long) (m - 1 - j) * idx;
                ans[idx] = left + right;
            }
        }
        return ans;
    }
}
