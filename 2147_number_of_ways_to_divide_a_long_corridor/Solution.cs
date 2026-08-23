// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

public class Solution {
    public int NumberOfWays(string corridor) {
        const int MOD = 1000000007;
        var seats = new List<int>();
        for (int i = 0; i < corridor.Length; i++)
            if (corridor[i] == 'S') seats.Add(i);
        if (seats.Count == 0 || seats.Count % 2 != 0) return 0;
        long ans = 1;
        for (int i = 2; i < seats.Count; i += 2)
            ans = ans * (seats[i] - seats[i - 1]) % MOD;
        return (int)ans;
    }
}
