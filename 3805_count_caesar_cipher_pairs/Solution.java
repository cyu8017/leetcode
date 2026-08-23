// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countPairs(String[] words) {
        var cnt = new HashMap<String, Integer>();
        for (String word : words) {
            char[] s = word.toCharArray();
            int k = 'z' - s[0];
            for (int i = 1; i < s.length; i++) {
                s[i] = (char)('a' + (s[i] - 'a' + k) % 26);
            }
            s[0] = 'z';
            String key = new String(s);
            if (!cnt.containsKey(key)) cnt.put(key, 0);
            cnt.merge(key, 1, Integer::sum);
        }
        long ans = 0;
        for (var v : cnt.values()) ans += (long)v * (v - 1) / 2;
        return ans;
    }
}
