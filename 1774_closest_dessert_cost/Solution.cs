// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

public class Solution {
    private int best;
    private int target;
    private int[] toppingCosts;

    public int ClosestCost(int[] baseCosts, int[] toppingCosts, int target) {
        this.best = int.MaxValue / 2;
        this.target = target;
        this.toppingCosts = toppingCosts;
        foreach (int baseCost in baseCosts) {
            Dfs(0, baseCost);
        }
        return best;
    }

    private void Dfs(int i, int cur) {
        int curDiff = System.Math.Abs(cur - target);
        int bestDiff = System.Math.Abs(best - target);
        if (curDiff < bestDiff || (curDiff == bestDiff && cur < best)) {
            best = cur;
        }
        if (i == toppingCosts.Length || cur >= target) {
            return;
        }
        Dfs(i + 1, cur);
        Dfs(i + 1, cur + toppingCosts[i]);
        Dfs(i + 1, cur + 2 * toppingCosts[i]);
    }
}
