// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

public class Solution {
    public int[] CountPairs(int n, int[][] edges, int[] queries) {
        var deg = new int[n + 1];
        var shared = new Dictionary<long, int>();
        foreach (var edge in edges) {
            int a = Math.Min(edge[0], edge[1]);
            int b = Math.Max(edge[0], edge[1]);
            deg[a]++;
            deg[b]++;
            long key = (long)a * 100000 + b;
            shared[key] = shared.GetValueOrDefault(key) + 1;
        }
        var sortedDeg = new int[n];
        Array.Copy(deg, 1, sortedDeg, 0, n);
        Array.Sort(sortedDeg);
        var ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int q = queries[qi];
            int res = 0;
            int left = 0;
            int right = n - 1;
            while (left < right) {
                if (sortedDeg[left] + sortedDeg[right] > q) {
                    res += right - left;
                    right--;
                } else {
                    left++;
                }
            }
            foreach (var entry in shared) {
                int a = (int)(entry.Key / 100000);
                int b = (int)(entry.Key % 100000);
                int sum = deg[a] + deg[b];
                if (sum > q && q >= sum - entry.Value) {
                    res--;
                }
            }
            ans[qi] = res;
        }
        return ans;
    }
}
