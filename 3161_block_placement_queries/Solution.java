// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    static class FenwickMax {
        int[] vals;

        FenwickMax(int n) {
            vals = new int[n + 1];
        }

        void maximize(int i, int val) {
            for (; i < vals.length; i += i & -i)
                vals[i] = Math.max(vals[i], val);
        }

        int get(int i) {
            int res = 0;
            for (; i > 0; i -= i & -i) res = Math.max(res, vals[i]);
            return res;
        }
    }

    private int lowerBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    public boolean[] getResults(int[][] queries) {
        int n = queries.length * 3;
        if (n > 50000) n = 50000;
        FenwickMax tree = new FenwickMax(n + 1);
        List<Integer> obs = new ArrayList<>();
        obs.add(0);
        obs.add(n);
        for (int[] q : queries) {
            if (q[0] == 1) {
                int x = q[1];
                int idx = lowerBound(obs, x);
                if (idx == obs.size() || obs.get(idx) != x) obs.add(idx, x);
            }
        }
        for (int i = 0; i + 1 < obs.size(); i++) {
            tree.maximize(obs.get(i + 1), obs.get(i + 1) - obs.get(i));
        }
        List<Boolean> ans = new ArrayList<>();
        for (int i = queries.length - 1; i >= 0; i--) {
            int typ = queries[i][0], x = queries[i][1];
            if (typ == 1) {
                int j = lowerBound(obs, x);
                int prev = obs.get(j - 1), next = obs.get(j + 1);
                obs.remove(j);
                tree.maximize(next, next - prev);
            } else {
                int sz = queries[i][2];
                int j = lowerBound(obs, x + 1) - 1;
                int prev = obs.get(j);
                ans.add(tree.get(prev) >= sz || x - prev >= sz);
            }
        }
        Collections.reverse(ans);
        boolean[] out = new boolean[ans.size()];
        for (int i = 0; i < ans.size(); i++) out[i] = ans.get(i);
        return out;
    }
}
