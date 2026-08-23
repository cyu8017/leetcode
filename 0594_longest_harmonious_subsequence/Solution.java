// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findLHS(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        int best = 0;
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            Integer next = counts.get(entry.getKey() + 1);
            if (next != null) {
                best = Math.max(best, entry.getValue() + next);
            }
        }
        return best;
    }
}
