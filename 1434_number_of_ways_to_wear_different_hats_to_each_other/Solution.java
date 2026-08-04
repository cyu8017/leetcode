// LeetCode 1434 - Number Of Ways To Wear Different Hats To Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

import java.util.*;

class Solution {
    public int numberWays(List<List<Integer>> hats) {
        int mod = 1_000_000_007, people = hats.size();
        List<List<Integer>> wearers = new ArrayList<>();
        for (int i = 0; i <= 40; i++) wearers.add(new ArrayList<>());
        for (int person = 0; person < people; person++) {
            for (int hat : hats.get(person)) wearers.get(hat).add(person);
        }
        int[] dp = new int[1 << people];
        dp[0] = 1;
        for (int hat = 1; hat <= 40; hat++) {
            int[] nxt = dp.clone();
            for (int mask = 0; mask < dp.length; mask++) {
                if (dp[mask] == 0) continue;
                for (int person : wearers.get(hat)) {
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
