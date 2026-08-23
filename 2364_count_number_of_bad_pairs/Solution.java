// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countBadPairs(int[] nums) {
        long n = nums.length;
        long total = n * (n - 1) / 2;
        Map<Integer, Long> freq = new HashMap<>();
        long good = 0;
        for (int i = 0; i < nums.length; i++) {
            int key = nums[i] - i;
            good += freq.getOrDefault(key, 0L);
            freq.put(key, freq.getOrDefault(key, 0L) + 1);
        }
        return total - good;
    }
}
