// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String majorityFrequencyGroup(String s) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        Map<Integer, StringBuilder> f = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            if (cnt[i] > 0)
                f.computeIfAbsent(cnt[i], x -> new StringBuilder()).append((char) ('a' + i));
        }
        int mx = 0, mv = 0;
        String ans = "";
        for (Map.Entry<Integer, StringBuilder> e : f.entrySet()) {
            int v = e.getKey();
            String cs = e.getValue().toString();
            if (cs.length() > mx || (cs.length() == mx && v > mv)) {
                mx = cs.length();
                mv = v;
                ans = cs;
            }
        }
        return ans;
    }
}
