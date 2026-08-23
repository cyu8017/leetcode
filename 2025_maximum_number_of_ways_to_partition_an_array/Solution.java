// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

import java.util.*;

class Solution {
    public int waysToPartition(int[] nums, int k) {
        int n = nums.length;
        long[] pref = new long[n];
        pref[0] = nums[0];
        for (int i = 1; i < n; i++) pref[i] = pref[i - 1] + nums[i];
        long total = pref[n - 1];
        Map<Long, Integer> right = new HashMap<>();
        Map<Long, Integer> left = new HashMap<>();
        for (int i = 0; i < n - 1; i++) right.merge(pref[i], 1, Integer::sum);
        int ans = 0;
        if (total % 2 == 0) ans = right.getOrDefault(total / 2, 0);
        for (int i = 0; i < n; i++) {
            long diff = (long) k - nums[i];
            long newTotal = total + diff;
            int cur = 0;
            if (newTotal % 2 == 0) {
                long half = newTotal / 2;
                cur = left.getOrDefault(half, 0) + right.getOrDefault(half - diff, 0);
            }
            ans = Math.max(ans, cur);
            if (i < n - 1) {
                left.merge(pref[i], 1, Integer::sum);
                right.put(pref[i], right.get(pref[i]) - 1);
            }
        }
        return ans;
    }
}
