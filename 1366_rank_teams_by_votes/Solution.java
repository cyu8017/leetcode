// LeetCode 1366 - Rank Teams By Votes
// https://leetcode.com/problems/rank-teams-by-votes/

import java.util.*;

class Solution {
    public String rankTeams(String[] votes) {
        int m = votes[0].length();
        Map<Character, int[]> count = new HashMap<>();
        for (char c : votes[0].toCharArray()) count.put(c, new int[m]);
        for (String v : votes) {
            for (int i = 0; i < v.length(); i++) count.get(v.charAt(i))[i]++;
        }
        List<Character> chars = new ArrayList<>(count.keySet());
        chars.sort((a, b) -> {
            int[] ca = count.get(a), cb = count.get(b);
            for (int i = 0; i < m; i++) {
                if (ca[i] != cb[i]) return Integer.compare(cb[i], ca[i]);
            }
            return Character.compare(a, b);
        });
        StringBuilder sb = new StringBuilder();
        for (char c : chars) sb.append(c);
        return sb.toString();
    }
}
