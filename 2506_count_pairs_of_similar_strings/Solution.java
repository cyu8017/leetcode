// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int similarPairs(String[] words) {
        Map<Integer, Integer> freq = new HashMap<>();
        int ans = 0;
        for (String w : words) {
            int mask = 0;
            for (char c : w.toCharArray()) mask |= 1 << (c - 'a');
            ans += freq.getOrDefault(mask, 0);
            freq.put(mask, freq.getOrDefault(mask, 0) + 1);
        }
        return ans;
    }
}
