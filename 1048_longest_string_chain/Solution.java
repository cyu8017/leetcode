// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestStrChain(String[] words) {
        Arrays.sort(words, (a, b) -> a.length() - b.length());
        Map<String, Integer> dp = new HashMap<>();
        int ans = 1;
        for (String w : words) {
            int best = 1;
            for (int i = 0; i < w.length(); i++) {
                String prev = w.substring(0, i) + w.substring(i + 1);
                best = Math.max(best, dp.getOrDefault(prev, 0) + 1);
            }
            dp.put(w, best);
            ans = Math.max(ans, best);
        }
        return ans;
    }
}
