// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

import java.util.*;

class Solution {
    public int[] recoverArray(int n, int[] sums) {
        Arrays.sort(sums);
        List<Integer> cur = new ArrayList<>();
        for (int x : sums) cur.add(x);
        int[] ans = new int[n];
        for (int t = 0; t < n; t++) {
            int d = cur.get(1) - cur.get(0);
            Map<Integer, Integer> count = new HashMap<>();
            for (int x : cur) count.merge(x, 1, Integer::sum);
            List<Integer> without = new ArrayList<>();
            List<Integer> withD = new ArrayList<>();
            for (int x : cur) {
                if (count.getOrDefault(x, 0) == 0) continue;
                count.merge(x, -1, Integer::sum);
                count.merge(x + d, -1, Integer::sum);
                without.add(x);
                withD.add(x + d);
            }
            if (without.contains(0)) {
                ans[t] = d;
                cur = without;
            } else {
                ans[t] = -d;
                cur = withD;
            }
        }
        return ans;
    }
}
