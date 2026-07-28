// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        List<Boolean> ans = new ArrayList<>(queries.length);
        for (String q : queries) ans.add(matches(q, pattern));
        return ans;
    }

    private boolean matches(String q, String pattern) {
        int i = 0;
        for (char ch : q.toCharArray()) {
            if (i < pattern.length() && ch == pattern.charAt(i)) i++;
            else if (ch >= 'A' && ch <= 'Z') return false;
        }
        return i == pattern.length();
    }
}
