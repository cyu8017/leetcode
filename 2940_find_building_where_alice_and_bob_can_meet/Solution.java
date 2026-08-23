// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] leftmostBuildingQueries(int[] heights, int[][] queries) {
        int qn = queries.length;
        int[] ans = new int[qn];
        for (int i = 0; i < qn; i++) ans[i] = -1;
        @SuppressWarnings("unchecked")
        List<int[]>[] buckets = new ArrayList[heights.length];
        for (int i = 0; i < heights.length; i++) buckets[i] = new ArrayList<>();
        for (int qi = 0; qi < qn; qi++) {
            int a = queries[qi][0], b = queries[qi][1];
            if (a > b) { int t = a; a = b; b = t; }
            if (a == b || heights[a] < heights[b]) {
                ans[qi] = b;
                continue;
            }
            buckets[b].add(new int[]{heights[a], qi});
        }
        List<int[]> st = new ArrayList<>();
        for (int i = heights.length - 1; i >= 0; i--) {
            for (int[] p : buckets[i]) {
                int h = p[0], qi = p[1];
                int lo = 0, hi = st.size() - 1, pos = -1;
                while (lo <= hi) {
                    int mid = (lo + hi) / 2;
                    if (st.get(mid)[0] > h) {
                        pos = st.get(mid)[1];
                        lo = mid + 1;
                    } else hi = mid - 1;
                }
                ans[qi] = pos;
            }
            while (!st.isEmpty() && st.get(st.size() - 1)[0] <= heights[i]) st.remove(st.size() - 1);
            st.add(new int[]{heights[i], i});
        }
        return ans;
    }
}
