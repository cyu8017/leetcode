// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countSubarrays(int[] nums, int k) {
        Map<Integer, Integer> pre = new HashMap<>();
        long ans = 0;
        for (int x : nums) {
            Map<Integer, Integer> cur = new HashMap<>();
            for (Map.Entry<Integer, Integer> kv : pre.entrySet()) {
                cur.merge(x & kv.getKey(), kv.getValue(), Integer::sum);
            }
            cur.merge(x, 1, Integer::sum);
            ans += cur.getOrDefault(k, 0);
            pre = cur;
        }
        return ans;
    }
}
