// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        Map<String, Integer> freq = new HashMap<>();
        int ans = 0;
        for (String w : words) {
            char[] ca = w.toCharArray();
            for (int i = 0, j = ca.length - 1; i < j; i++, j--) {
                char t = ca[i];
                ca[i] = ca[j];
                ca[j] = t;
            }
            String rev = new String(ca);
            int c = freq.getOrDefault(rev, 0);
            if (c > 0) {
                ans++;
                freq.put(rev, c - 1);
            } else {
                freq.put(w, freq.getOrDefault(w, 0) + 1);
            }
        }
        return ans;
    }
}
