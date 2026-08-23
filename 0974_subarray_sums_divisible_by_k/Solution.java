// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

import java.util.*;

class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        count.put(0, 1);
        int prefix = 0, ans = 0;
        for (int x : nums) {
            prefix = ((prefix + x) % k + k) % k;
            ans += count.getOrDefault(prefix, 0);
            count.put(prefix, count.getOrDefault(prefix, 0) + 1);
        }
        return ans;
    }
}
