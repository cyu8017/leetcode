// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long maxScore(int[] prices) {
        Map<Integer, Long> best = new HashMap<>();
        long ans = 0;
        for (int i = 0; i < prices.length; i++) {
            int key = prices[i] - (i + 1);
            long cand = best.getOrDefault(key, 0L) + prices[i];
            if (cand > best.getOrDefault(key, 0L)) best.put(key, cand);
            if (best.get(key) > ans) ans = best.get(key);
        }
        return ans;
    }
}
