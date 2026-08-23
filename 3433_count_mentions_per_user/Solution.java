// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        events.sort((a, b) -> {
            int ti = Integer.parseInt(a.get(1)), tj = Integer.parseInt(b.get(1));
            if (ti != tj) return Integer.compare(ti, tj);
            return b.get(0).compareTo(a.get(0));
        });
        boolean[] online = new boolean[numberOfUsers];
        Arrays.fill(online, true);
        int[] offlineUntil = new int[numberOfUsers];
        int[] ans = new int[numberOfUsers];
        for (List<String> e : events) {
            int t = Integer.parseInt(e.get(1));
            for (int i = 0; i < numberOfUsers; i++) {
                if (!online[i] && offlineUntil[i] <= t) online[i] = true;
            }
            if (e.get(0).equals("OFFLINE")) {
                int id = Integer.parseInt(e.get(2));
                online[id] = false;
                offlineUntil[id] = t + 60;
            } else {
                String msg = e.get(2);
                if (msg.equals("ALL")) {
                    for (int i = 0; i < numberOfUsers; i++) ans[i]++;
                } else if (msg.equals("HERE")) {
                    for (int i = 0; i < numberOfUsers; i++) if (online[i]) ans[i]++;
                } else {
                    for (String part : msg.split(" ")) {
                        int id = Integer.parseInt(part.substring(2));
                        ans[id]++;
                    }
                }
            }
        }
        return ans;
    }
}
