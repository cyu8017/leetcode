// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] countPairs(int n, int[][] edges, int[] queries) {
        int[] deg = new int[n + 1];
        Map<Long, Integer> shared = new HashMap<>();
        for (int[] edge : edges) {
            int a = Math.min(edge[0], edge[1]);
            int b = Math.max(edge[0], edge[1]);
            deg[a]++;
            deg[b]++;
            long key = (long) a * 100000 + b;
            shared.merge(key, 1, Integer::sum);
        }
        int[] sortedDeg = Arrays.copyOfRange(deg, 1, n + 1);
        Arrays.sort(sortedDeg);
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
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
            for (Map.Entry<Long, Integer> entry : shared.entrySet()) {
                int a = (int) (entry.getKey() / 100000);
                int b = (int) (entry.getKey() % 100000);
                int sum = deg[a] + deg[b];
                if (sum > q && q >= sum - entry.getValue()) {
                    res--;
                }
            }
            ans[qi] = res;
        }
        return ans;
    }
}
