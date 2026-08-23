// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long countInterestingSubarrays(List<Integer> nums, int modulo, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);
        long ans = 0;
        int pref = 0;
        for (int v : nums) {
            if (v % modulo == k) pref++;
            int need = (pref - k) % modulo;
            if (need < 0) need += modulo;
            ans += freq.getOrDefault(need, 0);
            freq.merge(pref % modulo, 1, Integer::sum);
        }
        return ans;
    }
}
