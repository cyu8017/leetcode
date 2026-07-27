// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

import java.util.*;

class Solution {
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        Map<String, List<Integer>> times = new HashMap<>();
        for (int i = 0; i < keyName.length; i++) {
            String[] parts = keyTime[i].split(":");
            int mins = Integer.parseInt(parts[0]) * 60 + Integer.parseInt(parts[1]);
            times.computeIfAbsent(keyName[i], k -> new ArrayList<>()).add(mins);
        }
        List<String> ans = new ArrayList<>();
        for (Map.Entry<String, List<Integer>> e : times.entrySet()) {
            List<Integer> a = e.getValue();
            Collections.sort(a);
            for (int i = 0; i + 2 < a.size(); i++) {
                if (a.get(i + 2) - a.get(i) <= 60) {
                    ans.add(e.getKey());
                    break;
                }
            }
        }
        Collections.sort(ans);
        return ans;
    }
}
