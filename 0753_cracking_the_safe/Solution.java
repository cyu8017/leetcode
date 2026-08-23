// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

import java.util.*;

class Solution {
    private final Set<String> seen = new HashSet<>();
    private final List<Character> path = new ArrayList<>();

    public String crackSafe(int n, int k) {
        seen.clear();
        path.clear();
        StringBuilder startSb = new StringBuilder();
        for (int i = 0; i < n - 1; i++) startSb.append('0');
        String start = startSb.toString();
        dfs(start, k);
        StringBuilder result = new StringBuilder();
        for (char ch : path) result.append(ch);
        return result.toString() + start;
    }

    private void dfs(String node, int k) {
        for (int d = 0; d < k; d++) {
            char digit = (char) ('0' + d);
            String edge = node + digit;
            if (seen.add(edge)) {
                dfs(edge.substring(1), k);
                path.add(digit);
            }
        }
    }
}
