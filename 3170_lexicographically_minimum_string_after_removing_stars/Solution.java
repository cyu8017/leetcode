// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String clearStars(String s) {
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[26];
        for (int i = 0; i < 26; i++) g[i] = new ArrayList<>();
        int n = s.length();
        boolean[] rem = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '*') {
                rem[i] = true;
                for (int j = 0; j < 26; j++) {
                    if (!g[j].isEmpty()) {
                        rem[g[j].get(g[j].size() - 1)] = true;
                        g[j].remove(g[j].size() - 1);
                        break;
                    }
                }
            } else {
                g[s.charAt(i) - 'a'].add(i);
            }
        }
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < n; i++) if (!rem[i]) ans.append(s.charAt(i));
        return ans.toString();
    }
}
