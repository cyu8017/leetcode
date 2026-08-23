// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int maxRequests(int[][] requests, int k, int window) {
        var g = new HashMap<Integer, List<Integer>>();
        for (var r : requests.entrySet()) {
            if (!g.containsKey(r[0])) g.put(r[0], new ArrayList<Integer>());
            g.get(r[0]).add(r[1]);
        }
        int ans = requests.length;
        for (var ts : g.values()) {
            ts.sort(null);
            var kept = new ArrayList<Integer>();
            for (int t : ts) {
                while (kept.size() > 0 && t - kept.get(0) > window) kept.remove(0);
                if (kept.size() < k) kept.add(t);
                else ans--;
            }
        }
        return ans;
    }
}
