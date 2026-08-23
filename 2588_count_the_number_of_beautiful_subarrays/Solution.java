// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long beautifulSubarrays(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);
        int xorv = 0;
        long ans = 0;
        for (int x : nums) {
            xorv ^= x;
            ans += freq.getOrDefault(xorv, 0);
            freq.put(xorv, freq.getOrDefault(xorv, 0) + 1);
        }
        return ans;
    }
}
