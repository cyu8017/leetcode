// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] simulationResult(int[] windows, int[] queries) {
        int n = windows.length;
        boolean[] s = new boolean[n + 1];
        List<Integer> ans = new ArrayList<>();
        for (int i = queries.length - 1; i >= 0; i--) {
            int q = queries[i];
            if (!s[q]) {
                s[q] = true;
                ans.add(q);
            }
        }
        for (int w : windows) {
            if (!s[w]) ans.add(w);
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }
}
