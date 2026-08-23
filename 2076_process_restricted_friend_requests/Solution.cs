// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

public class Solution {
    public bool[] FriendRequests(int n, int[][] restrictions, int[][] requests) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int Find(int x) => parent[x] == x ? x : parent[x] = Find(parent[x]);
        void Unite(int a, int b) {
            a = Find(a); b = Find(b);
            if (a != b) parent[a] = b;
        }
        bool[] ans = new bool[requests.Length];
        for (int i = 0; i < requests.Length; i++) {
            int u = Find(requests[i][0]), v = Find(requests[i][1]);
            bool ok = true;
            if (u != v) {
                foreach (var r in restrictions) {
                    int x = Find(r[0]), y = Find(r[1]);
                    if ((x == u && y == v) || (x == v && y == u)) { ok = false; break; }
                }
            }
            ans[i] = ok;
            if (ok) Unite(u, v);
        }
        return ans;
    }
}
