// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

import java.util.*;

class Solution {
    public int maxUniqueSplit(String s) {
        Set<String> used = new HashSet<>();
        int[] answer = new int[1];
        dfs(s, 0, used, answer);
        return answer[0];
    }

    private void dfs(String s, int i, Set<String> used, int[] answer) {
        if (used.size() + s.length() - i <= answer[0]) {
            return;
        }
        if (i == s.length()) {
            answer[0] = Math.max(answer[0], used.size());
            return;
        }
        for (int j = i + 1; j <= s.length(); j++) {
            String part = s.substring(i, j);
            if (!used.contains(part)) {
                used.add(part);
                dfs(s, j, used, answer);
                used.remove(part);
            }
        }
    }
}
