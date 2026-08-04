// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

import java.util.*;

class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, int[][] edges) {
        boolean[] incoming = new boolean[n];
        for (int[] e : edges) {
            incoming[e[1]] = true;
        }
        List<Integer> ans = new ArrayList<>();
        for (int v = 0; v < n; v++) {
            if (!incoming[v]) {
                ans.add(v);
            }
        }
        return ans;
    }
}
