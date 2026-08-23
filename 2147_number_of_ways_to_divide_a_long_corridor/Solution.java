// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

import java.util.*;

class Solution {
    public int numberOfWays(String corridor) {
        final int MOD = 1_000_000_007;
        List<Integer> seats = new ArrayList<>();
        for (int i = 0; i < corridor.length(); i++)
            if (corridor.charAt(i) == 'S') seats.add(i);
        if (seats.isEmpty() || seats.size() % 2 != 0) return 0;
        long ans = 1;
        for (int i = 2; i < seats.size(); i += 2)
            ans = ans * (seats.get(i) - seats.get(i - 1)) % MOD;
        return (int) ans;
    }
}
