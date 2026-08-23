// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

public class Solution {
    public int MinimumCost(int[] cost) {
        Array.Sort(cost, (a, b) => b.CompareTo(a));
        int ans = 0;
        for (int i = 0; i < cost.Length; i++)
            if (i % 3 != 2) ans += cost[i];
        return ans;
    }
}
