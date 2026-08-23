// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

import java.util.List;

class Solution {
    public int maxNumberOfAlloys(int n, int k, int budget, List<List<Integer>> composition,
                                 List<Integer> stock, List<Integer> cost) {
        long lo = 0, hi = 1000000000L, ans = 0;
        while (lo <= hi) {
            long mid = (lo + hi) / 2;
            if (ok(mid, n, budget, composition, stock, cost)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return (int) ans;
    }

    private boolean ok(long machines, int n, int budget, List<List<Integer>> composition,
                       List<Integer> stock, List<Integer> cost) {
        for (List<Integer> comp : composition) {
            long spend = 0;
            for (int i = 0; i < n; i++) {
                long need = machines * comp.get(i) - stock.get(i);
                if (need > 0) spend += need * cost.get(i);
            }
            if (spend <= budget) return true;
        }
        return false;
    }
}
