// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    private int[] parent;

    private static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    private void unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra != rb) parent[ra] = rb;
    }

    public int countComponents(int[] nums, int threshold) {
        int n = nums.length;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        Map<Integer, Integer> idx = new HashMap<>();
        for (int i = 0; i < n; i++) idx.put(nums[i], i);
        for (int d = 1; d <= threshold; d++) {
            int first = -1;
            for (int m = d; m <= threshold; m += d) {
                Integer i = idx.get(m);
                if (i != null) {
                    if (first == -1) first = i;
                    else if ((long) nums[first] * nums[i] / gcd(nums[first], nums[i]) <= threshold)
                        unite(first, i);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = nums[i], b = nums[j];
                int g = gcd(a, b);
                if ((long) a / g * b <= threshold) unite(i, j);
            }
        }
        Set<Integer> comp = new HashSet<>();
        for (int i = 0; i < n; i++) comp.add(find(i));
        return comp.size();
    }
}
