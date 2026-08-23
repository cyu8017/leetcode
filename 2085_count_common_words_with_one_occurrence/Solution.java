// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

import java.util.*;

class Solution {
    public int countWords(String[] words1, String[] words2) {
        Map<String, Integer> f1 = new HashMap<>();
        Map<String, Integer> f2 = new HashMap<>();
        for (String w : words1) f1.merge(w, 1, Integer::sum);
        for (String w : words2) f2.merge(w, 1, Integer::sum);
        int ans = 0;
        for (Map.Entry<String, Integer> kv : f1.entrySet())
            if (kv.getValue() == 1 && f2.getOrDefault(kv.getKey(), 0) == 1) ans++;
        return ans;
    }
}
