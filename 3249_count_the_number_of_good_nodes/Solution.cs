// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

using System.Collections.Generic;

public class Solution {
    public int CountGoodNodes(int[][] edges) {
        int n = edges.Length + 1;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int ans = 0;
        int Dfs(int a, int fa) {
            int pre = -1, cnt = 1, ok = 1;
            foreach (int b in g[a]) {
                if (b != fa) {
                    int cur = Dfs(b, a);
                    cnt += cur;
                    if (pre < 0) pre = cur;
                    else if (pre != cur) ok = 0;
                }
            }
            ans += ok;
            return cnt;
        }
        Dfs(0, -1);
        return ans;
    }
}
