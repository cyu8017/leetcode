// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum_subarray_length_with_distinct_sum_at_least_k/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minLength(int[] nums, int k) {
        int n = nums.length;
        int ans = n + 1, l = 0;
        Map<Integer, Integer> cnt = new HashMap<>();
        long s = 0;
        for (int r = 0; r < n; r++) {
            int c = cnt.merge(nums[r], 1, Integer::sum);
            if (c == 1) s += nums[r];
            while (s >= k) {
                if (r - l + 1 < ans) ans = r - l + 1;
                int left = nums[l];
                int nc = cnt.merge(left, -1, Integer::sum);
                if (nc == 0) {
                    cnt.remove(left);
                    s -= left;
                }
                l++;
            }
        }
        return ans > n ? -1 : ans;
    }
}
