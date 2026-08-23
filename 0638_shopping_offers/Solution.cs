// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    private int[] price;
    private int[][] special;
    private readonly Dictionary<string, int> memo = new();

    public int ShoppingOffers(IList<int> price, IList<IList<int>> special, IList<int> needs) {
        this.price = price.ToArray();
        this.special = special.Select(s => s.ToArray()).ToArray();
        memo.Clear();
        return Dfs(needs.ToArray());
    }

    private int Dfs(int[] state) {
        string key = string.Join(",", state);
        if (memo.TryGetValue(key, out int cached)) return cached;
        int cost = 0;
        for (int i = 0; i < price.Length; ++i) cost += state[i] * price[i];
        foreach (int[] offer in special) {
            int[] nxt = (int[])state.Clone();
            bool valid = true;
            for (int i = 0; i < price.Length; ++i) {
                if (nxt[i] < offer[i]) { valid = false; break; }
                nxt[i] -= offer[i];
            }
            if (valid) {
                int candidate = offer[price.Length] + Dfs(nxt);
                if (candidate < cost) cost = candidate;
            }
        }
        return memo[key] = cost;
    }
}
