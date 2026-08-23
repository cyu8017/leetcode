// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    int[] parent;

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra != rb) {
            if (ra < rb) parent[rb] = ra;
            else parent[ra] = rb;
        }
    }

    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        parent = new int[c + 1];
        for (int i = 0; i <= c; i++) parent[i] = i;
        for (int[] e : connections) unite(e[0], e[1]);
        boolean[] online = new boolean[c + 1];
        java.util.Arrays.fill(online, true);
        Map<Integer, List<Integer>> comp = new HashMap<>();
        for (int i = 1; i <= c; i++) comp.computeIfAbsent(find(i), k -> new ArrayList<>()).add(i);
        for (List<Integer> ids : comp.values()) Collections.sort(ids);
        Map<Integer, Integer> ptr = new HashMap<>();
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            int t = q[0], x = q[1];
            if (t == 2) {
                online[x] = false;
                continue;
            }
            if (online[x]) {
                ans.add(x);
                continue;
            }
            int r = find(x);
            List<Integer> ids = comp.get(r);
            int p = ptr.getOrDefault(r, 0);
            while (p < ids.size() && !online[ids.get(p)]) p++;
            ptr.put(r, p);
            ans.add(p < ids.size() ? ids.get(p) : -1);
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
