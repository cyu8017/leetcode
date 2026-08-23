// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

public class Solution {
    public int CountHousePlacements(int n) {
        const int mod = 1000000007;
        long a = 1, b = 1;
        for (int i = 1; i <= n; ++i) {
            long na = (a + b) % mod;
            b = a;
            a = na;
        }
        long ways = (a + b) % mod;
        return (int)(ways * ways % mod);
    }
}
