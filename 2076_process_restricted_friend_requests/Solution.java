// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

class Solution {
    private int[] parent;

    public boolean[] friendRequests(int n, int[][] restrictions, int[][] requests) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        boolean[] ans = new boolean[requests.length];
        for (int i = 0; i < requests.length; i++) {
            int u = find(requests[i][0]), v = find(requests[i][1]);
            boolean ok = true;
            if (u != v) {
                for (int[] r : restrictions) {
                    int x = find(r[0]), y = find(r[1]);
                    if ((x == u && y == v) || (x == v && y == u)) { ok = false; break; }
                }
            }
            ans[i] = ok;
            if (ok) unite(u, v);
        }
        return ans;
    }

    private int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    private void unite(int a, int b) {
        a = find(a); b = find(b);
        if (a != b) parent[a] = b;
    }
}
