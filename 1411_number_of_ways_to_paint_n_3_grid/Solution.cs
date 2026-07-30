// LeetCode 1411 - Number Of Ways To Paint N 3 Grid
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

public class Solution {
    public int NumOfWays(int n) {
        long mod = 1000000007, aba = 6, abc = 6;
        for (int i = 1; i < n; i++) {
            long nAba = (3 * aba + 2 * abc) % mod;
            long nAbc = (2 * aba + 2 * abc) % mod;
            aba = nAba; abc = nAbc;
        }
        return (int)((aba + abc) % mod);
    }
}
