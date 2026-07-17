// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

class Solution {
    private int best;
    private int target;
    private int[] toppingCosts;

    public int closestCost(int[] baseCosts, int[] toppingCosts, int target) {
        this.best = Integer.MAX_VALUE / 2;
        this.target = target;
        this.toppingCosts = toppingCosts;
        for (int base : baseCosts) {
            dfs(0, base);
        }
        return best;
    }

    private void dfs(int i, int cur) {
        int curDiff = Math.abs(cur - target);
        int bestDiff = Math.abs(best - target);
        if (curDiff < bestDiff || (curDiff == bestDiff && cur < best)) {
            best = cur;
        }
        if (i == toppingCosts.length || cur >= target) {
            return;
        }
        dfs(i + 1, cur);
        dfs(i + 1, cur + toppingCosts[i]);
        dfs(i + 1, cur + 2 * toppingCosts[i]);
    }
}
