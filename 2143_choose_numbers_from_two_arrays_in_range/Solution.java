// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

import java.util.*;

class Solution {
    public int countSubranges(int[] nums1, int[] nums2) {
        final int MOD = 1_000_000_007;
        int n = nums1.length, ans = 0;
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < n; i++) {
            Map<Integer, Integer> ndp = new HashMap<>();
            ndp.put(nums1[i], (ndp.getOrDefault(nums1[i], 0) + 1) % MOD);
            ndp.put(-nums2[i], (ndp.getOrDefault(-nums2[i], 0) + 1) % MOD);
            for (Map.Entry<Integer, Integer> kv : dp.entrySet()) {
                int diff = kv.getKey(), cnt = kv.getValue();
                ndp.put(diff + nums1[i], (ndp.getOrDefault(diff + nums1[i], 0) + cnt) % MOD);
                ndp.put(diff - nums2[i], (ndp.getOrDefault(diff - nums2[i], 0) + cnt) % MOD);
            }
            dp = ndp;
            ans = (ans + dp.getOrDefault(0, 0)) % MOD;
        }
        return ans;
    }
}
