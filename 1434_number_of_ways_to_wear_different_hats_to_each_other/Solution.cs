// LeetCode 1434 - Number Of Ways To Wear Different Hats To Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

using System.Collections.Generic;
public class Solution {
    public int NumberWays(IList<IList<int>> hats) {
        int mod = 1000000007, people = hats.Count;
        var wearers = new List<int>[41];
        for (int i = 0; i < 41; i++) wearers[i] = new List<int>();
        for (int person = 0; person < people; person++)
            foreach (int hat in hats[person]) wearers[hat].Add(person);
        var dp = new int[1 << people]; dp[0] = 1;
        for (int hat = 1; hat <= 40; hat++) {
            var nxt = (int[])dp.Clone();
            for (int mask = 0; mask < dp.Length; mask++) {
                if (dp[mask] == 0) continue;
                foreach (int person in wearers[hat]) {
                    if (((mask >> person) & 1) == 0) {
                        int nm = mask | (1 << person);
                        nxt[nm] = (nxt[nm] + dp[mask]) % mod;
                    }
                }
            }
            dp = nxt;
        }
        return dp[(1 << people) - 1];
    }
}
