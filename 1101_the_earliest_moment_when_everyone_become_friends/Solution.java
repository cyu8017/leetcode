// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

import java.util.*;

class Solution {
    public int earliestAcq(int[][] logs, int n) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        Arrays.sort(logs, (a, b) -> Integer.compare(a[0], b[0]));
        int components = n;
        for (int[] log : logs) {
            if (union(parent, log[1], log[2])) {
                components--;
                if (components == 1) return log[0];
            }
        }
        return -1;
    }

    private int find(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private boolean union(int[] parent, int a, int b) {
        int ra = find(parent, a), rb = find(parent, b);
        if (ra == rb) return false;
        parent[rb] = ra;
        return true;
    }
}
