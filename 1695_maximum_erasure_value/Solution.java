// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        Map<Integer, Integer> seen = new HashMap<>();
        int left = 0;
        int cur = 0;
        int best = 0;
        for (int right = 0; right < nums.length; right++) {
            int x = nums[right];
            if (seen.containsKey(x) && seen.get(x) >= left) {
                int stop = seen.get(x);
                while (left <= stop) {
                    cur -= nums[left++];
                }
            }
            seen.put(x, right);
            cur += x;
            best = Math.max(best, cur);
        }
        return best;
    }
}
