// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

import java.util.TreeMap;

class Solution {
    private void merge(TreeMap<Integer, Integer> st, int x, int v) {
        int nv = st.getOrDefault(x, 0) + v;
        if (nv == 0) st.remove(x);
        else st.put(x, nv);
    }

    public int minimumDistance(int[][] points) {
        TreeMap<Integer, Integer> st1 = new TreeMap<>();
        TreeMap<Integer, Integer> st2 = new TreeMap<>();
        for (int[] p : points) {
            merge(st1, p[0] + p[1], 1);
            merge(st2, p[0] - p[1], 1);
        }
        int ans = Integer.MAX_VALUE;
        for (int[] p : points) {
            int x = p[0], y = p[1];
            merge(st1, x + y, -1);
            merge(st2, x - y, -1);
            ans = Math.min(ans, Math.max(st1.lastKey() - st1.firstKey(), st2.lastKey() - st2.firstKey()));
            merge(st1, x + y, 1);
            merge(st2, x - y, 1);
        }
        return ans;
    }
}
