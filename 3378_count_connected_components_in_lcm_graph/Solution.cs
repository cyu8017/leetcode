// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

using System.Collections.Generic;

public class Solution {
    static int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int CountComponents(int[] nums, int threshold) {
        int n = nums.Length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        void Unite(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra != rb) parent[ra] = rb;
        }
        var idx = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) idx[nums[i]] = i;
        for (int d = 1; d <= threshold; d++) {
            int first = -1;
            for (int m = d; m <= threshold; m += d) {
                if (idx.TryGetValue(m, out int i)) {
                    if (first == -1) first = i;
                    else if ((long)nums[first] * nums[i] / Gcd(nums[first], nums[i]) <= threshold)
                        Unite(first, i);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = nums[i], b = nums[j];
                int g = Gcd(a, b);
                if ((long)a / g * b <= threshold) Unite(i, j);
            }
        }
        var comp = new HashSet<int>();
        for (int i = 0; i < n; i++) comp.Add(Find(i));
        return comp.Count;
    }
}
