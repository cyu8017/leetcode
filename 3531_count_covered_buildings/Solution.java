// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int countCoveredBuildings(int n, int[][] buildings) {
        Map<Integer, List<Integer>> g1 = new HashMap<>();
        Map<Integer, List<Integer>> g2 = new HashMap<>();
        for (int[] b : buildings) {
            g1.computeIfAbsent(b[0], k -> new ArrayList<>()).add(b[1]);
            g2.computeIfAbsent(b[1], k -> new ArrayList<>()).add(b[0]);
        }
        for (List<Integer> list : g1.values()) Collections.sort(list);
        for (List<Integer> list : g2.values()) Collections.sort(list);
        int ans = 0;
        for (int[] b : buildings) {
            int x = b[0], y = b[1];
            List<Integer> l1 = g1.get(x);
            List<Integer> l2 = g2.get(y);
            if (l2.get(0) < x && x < l2.get(l2.size() - 1) && l1.get(0) < y && y < l1.get(l1.size() - 1)) ans++;
        }
        return ans;
    }
}
