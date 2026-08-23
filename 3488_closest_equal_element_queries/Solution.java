// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        Map<Integer, List<Integer>> pos = new HashMap<>();
        for (int i = 0; i < n; i++) pos.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int idx = queries[qi];
            int x = nums[idx];
            List<Integer> arr = pos.get(x);
            if (arr.size() == 1) { ans[qi] = -1; continue; }
            int best = n;
            for (int p : arr) {
                if (p == idx) continue;
                int d = Math.abs(p - idx);
                d = Math.min(d, n - d);
                if (d < best) best = d;
            }
            ans[qi] = best;
        }
        return ans;
    }
}
