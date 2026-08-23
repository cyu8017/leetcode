// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public String findCommonResponse(List<List<String>> responses) {
        Map<String, Integer> cnt = new HashMap<>();
        for (List<String> ws : responses) {
            Set<String> s = new HashSet<>();
            for (String w : ws) {
                if (s.add(w)) cnt.merge(w, 1, Integer::sum);
            }
        }
        String ans = responses.get(0).get(0);
        for (Map.Entry<String, Integer> e : cnt.entrySet()) {
            String w = e.getKey();
            int v = e.getValue();
            if (cnt.get(ans) < v || (cnt.get(ans) == v && w.compareTo(ans) < 0)) ans = w;
        }
        return ans;
    }
}
