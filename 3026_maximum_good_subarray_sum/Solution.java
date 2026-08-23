// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        Map<Integer, Long> p = new HashMap<>();
        p.put(nums[0], 0L);
        long s = 0;
        int n = nums.length;
        long ans = Long.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            s += nums[i];
            if (p.containsKey(nums[i] - k)) ans = Math.max(ans, s - p.get(nums[i] - k));
            if (p.containsKey(nums[i] + k)) ans = Math.max(ans, s - p.get(nums[i] + k));
            if (i + 1 == n) break;
            Long old = p.get(nums[i + 1]);
            if (old == null || s < old) p.put(nums[i + 1], s);
        }
        return ans == Long.MIN_VALUE ? 0 : ans;
    }
}
