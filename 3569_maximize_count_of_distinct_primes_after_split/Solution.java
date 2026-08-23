// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] maximumCount(int[] nums, int[][] queries) {
        int mx = 0;
        for (int v : nums) mx = Math.max(mx, v);
        for (int[] q : queries) mx = Math.max(mx, q[1]);
        boolean[] isP = new boolean[mx + 1];
        for (int i = 2; i <= mx; i++) isP[i] = true;
        for (int i = 2; i * i <= mx; i++) {
            if (isP[i]) for (int j = i * i; j <= mx; j += i) isP[j] = false;
        }
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            nums[queries[qi][0]] = queries[qi][1];
            int best = 0;
            Map<Integer, Integer> left = new HashMap<>();
            Map<Integer, Integer> right = new HashMap<>();
            for (int v : nums) if (v <= mx && isP[v]) right.merge(v, 1, Integer::sum);
            for (int i = 0; i < nums.length - 1; i++) {
                int v = nums[i];
                if (v <= mx && isP[v]) {
                    left.merge(v, 1, Integer::sum);
                    int c = right.get(v) - 1;
                    if (c == 0) right.remove(v);
                    else right.put(v, c);
                }
                best = Math.max(best, left.size() + right.size());
            }
            ans[qi] = best;
        }
        return ans;
    }
}
