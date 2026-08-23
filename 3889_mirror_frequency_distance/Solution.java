// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int mirrorFrequency(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) freq.put(c, freq.getOrDefault(c, 0) + 1);
        int ans = 0;
        Map<Character, Boolean> vis = new HashMap<>();
        for (Map.Entry<Character, Integer> kv : freq.entrySet()) {
            char c = kv.getKey();
            int v = kv.getValue();
            char m;
            if (c >= 'a' && c <= 'z') m = (char) ('a' + 25 - (c - 'a'));
            else m = (char) ('0' + (9 - (c - '0')));
            if (Boolean.TRUE.equals(vis.get(m))) continue;
            vis.put(c, true);
            int mv = freq.getOrDefault(m, 0);
            ans += Math.abs(v - mv);
        }
        return ans;
    }
}
