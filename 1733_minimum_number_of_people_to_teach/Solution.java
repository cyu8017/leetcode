// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        int users = languages.length;
        boolean[][] knows = new boolean[users][n + 1];
        for (int user = 0; user < users; user++) {
            for (int lang : languages[user]) {
                knows[user][lang] = true;
            }
        }
        Set<Integer> need = new HashSet<>();
        for (int[] friendship : friendships) {
            int u = friendship[0] - 1;
            int v = friendship[1] - 1;
            boolean shares = false;
            for (int lang : languages[u]) {
                if (knows[v][lang]) {
                    shares = true;
                    break;
                }
            }
            if (!shares) {
                need.add(u);
                need.add(v);
            }
        }
        if (need.isEmpty()) {
            return 0;
        }
        int best = Integer.MAX_VALUE;
        for (int lang = 1; lang <= n; lang++) {
            int teach = 0;
            for (int user : need) {
                if (!knows[user][lang]) teach++;
            }
            best = Math.min(best, teach);
        }
        return best;
    }
}
