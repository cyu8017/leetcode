// LeetCode 1319 - Number Of Operations To Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] e : connections) {
            int ra = find(parent, e[0]), rb = find(parent, e[1]);
            if (ra != rb) parent[ra] = rb;
        }
        int comps = 0;
        for (int i = 0; i < n; i++) if (find(parent, i) == i) comps++;
        return comps - 1;
    }

    private int find(int[] parent, int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
}
