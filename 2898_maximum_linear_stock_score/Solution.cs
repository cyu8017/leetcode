// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

using System.Collections.Generic;

public class Solution {
    public long MaxScore(int[] prices) {
        var best = new Dictionary<int, long>();
        long ans = 0;
        for (int i = 0; i < prices.Length; i++) {
            int key = prices[i] - (i + 1);
            if (!best.ContainsKey(key)) best[key] = 0;
            long cand = best[key] + prices[i];
            if (cand > best[key]) best[key] = cand;
            if (best[key] > ans) ans = best[key];
        }
        return ans;
    }
}
