// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

public class Solution {
    public int StringCount(int n) {
        const int mod = 1000000007;
        int ModPow(long a, int b) {
            long res = 1;
            a %= mod;
            while (b > 0) {
                if ((b & 1) != 0) res = res * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return (int)res;
        }
        if (n < 4) return 0;
        long ans = ModPow(26, n);
        ans = (ans - 3L * ModPow(25, n) % mod + mod) % mod;
        ans = (ans + 3L * ModPow(24, n) % mod) % mod;
        ans = (ans - ModPow(23, n) + mod) % mod;
        ans = (ans + 1L * (n % mod) * ModPow(25, n - 1) % mod) % mod;
        ans = (ans - 2L * (n % mod) % mod * ModPow(24, n - 1) % mod + mod) % mod;
        ans = (ans + 1L * (n % mod) * ModPow(23, n - 1) % mod) % mod;
        ans = (ans - 1L * (n % mod) * ((n - 1 + mod) % mod) % mod * ModPow(24, n - 2) % mod % mod + mod) % mod;
        ans = (ans + 1L * (n % mod) * ((n - 1 + mod) % mod) % mod * ModPow(23, n - 2) % mod) % mod;
        return (int)ans;
    }
}
