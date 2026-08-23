// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int prefixConnected(String[] words, int k) {
        Map<String, Integer> cnt = new HashMap<>();
        for (String w : words) {
            if (w.length() >= k) {
                String p = w.substring(0, k);
                cnt.put(p, cnt.getOrDefault(p, 0) + 1);
            }
        }
        int ans = 0;
        for (int v : cnt.values()) if (v > 1) ans++;
        return ans;
    }
}
