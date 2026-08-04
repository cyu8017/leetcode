// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

import java.util.*;

class Solution {
    public List<String> mostVisitedPattern(String[] username, int[] timestamp, String[] website) {
        Map<String, List<int[]>> visits = new HashMap<>();
        for (int i = 0; i < username.length; i++) {
            visits.computeIfAbsent(username[i], k -> new ArrayList<>()).add(new int[]{timestamp[i], i});
        }
        Map<String, Integer> scores = new HashMap<>();
        for (List<int[]> list : visits.values()) {
            list.sort((a, b) -> Integer.compare(a[0], b[0]));
            List<String> sites = new ArrayList<>();
            for (int[] p : list) sites.add(website[p[1]]);
            Set<String> patterns = new HashSet<>();
            int m = sites.size();
            for (int i = 0; i < m; i++)
                for (int j = i + 1; j < m; j++)
                    for (int k = j + 1; k < m; k++)
                        patterns.add(sites.get(i) + "," + sites.get(j) + "," + sites.get(k));
            for (String p : patterns) scores.merge(p, 1, Integer::sum);
        }
        String best = null;
        int bestCount = -1;
        for (Map.Entry<String, Integer> e : scores.entrySet()) {
            if (e.getValue() > bestCount || (e.getValue() == bestCount && (best == null || e.getKey().compareTo(best) < 0))) {
                bestCount = e.getValue();
                best = e.getKey();
            }
        }
        return Arrays.asList(best.split(",", -1));
    }
}
