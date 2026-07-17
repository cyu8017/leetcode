// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

public class Solution {
    private int[] parent;

    public int MinimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.Length;
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        foreach (var swap in allowedSwaps) {
            Union(swap[0], swap[1]);
        }
        var groups = new Dictionary<int, Dictionary<int, int>>();
        for (int i = 0; i < n; i++) {
            int root = Find(i);
            if (!groups.ContainsKey(root)) {
                groups[root] = new Dictionary<int, int>();
            }
            var counts = groups[root];
            counts[source[i]] = counts.GetValueOrDefault(source[i]) + 1;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            var counts = groups[Find(i)];
            int remaining = counts.GetValueOrDefault(target[i]);
            if (remaining > 0) {
                counts[target[i]] = remaining - 1;
            } else {
                ans++;
            }
        }
        return ans;
    }

    private int Find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void Union(int a, int b) {
        int ra = Find(a);
        int rb = Find(b);
        if (ra != rb) {
            parent[rb] = ra;
        }
    }
}
