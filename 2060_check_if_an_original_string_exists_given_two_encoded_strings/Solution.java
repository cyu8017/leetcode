// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

import java.util.*;

class Solution {
    private String s1, s2;
    private final Map<String, Boolean> memo = new HashMap<>();

    public boolean possiblyEquals(String s1, String s2) {
        this.s1 = s1;
        this.s2 = s2;
        memo.clear();
        return dfs(0, 0, 0);
    }

    private boolean isDigit(char c) { return c >= '0' && c <= '9'; }

    private boolean dfs(int i, int j, int diff) {
        String key = i + "," + j + "," + diff;
        if (memo.containsKey(key)) return memo.get(key);
        int n = s1.length(), m = s2.length();
        if (i == n && j == m) { memo.put(key, diff == 0); return diff == 0; }
        boolean res = false;
        if (diff == 0 && i < n && j < m && !isDigit(s1.charAt(i)) && !isDigit(s2.charAt(j))) {
            if (s1.charAt(i) == s2.charAt(j)) res = dfs(i + 1, j + 1, 0);
        } else if (diff > 0 && i < n && !isDigit(s1.charAt(i))) {
            res = dfs(i + 1, j, diff - 1);
        } else if (diff < 0 && j < m && !isDigit(s2.charAt(j))) {
            res = dfs(i, j + 1, diff + 1);
        }
        if (!res && i < n && isDigit(s1.charAt(i))) {
            int val = 0;
            for (int p = i; p < n && isDigit(s1.charAt(p)); p++) {
                val = val * 10 + (s1.charAt(p) - '0');
                if (dfs(p + 1, j, diff + val)) { res = true; break; }
            }
        }
        if (!res && j < m && isDigit(s2.charAt(j))) {
            int val = 0;
            for (int p = j; p < m && isDigit(s2.charAt(p)); p++) {
                val = val * 10 + (s2.charAt(p) - '0');
                if (dfs(i, p + 1, diff - val)) { res = true; break; }
            }
        }
        memo.put(key, res);
        return res;
    }
}
