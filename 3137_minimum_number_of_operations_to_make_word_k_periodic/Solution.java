// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minimumOperationsToMakeKPeriodic(String word, int k) {
        Map<String, Integer> cnt = new HashMap<>();
        int n = word.length(), mx = 0;
        for (int i = 0; i < n; i += k) {
            String s = word.substring(i, i + k);
            int v = cnt.getOrDefault(s, 0) + 1;
            cnt.put(s, v);
            mx = Math.max(mx, v);
        }
        return n / k - mx;
    }
}
