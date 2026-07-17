// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

public class Solution {
    public int CountHomogenous(string s) {
        const long MOD = 1000000007L;
        long ans = 0;
        int i = 0;
        while (i < s.Length) {
            int j = i;
            while (j < s.Length && s[j] == s[i]) {
                j++;
            }
            long length = j - i;
            ans = (ans + length * (length + 1) / 2) % MOD;
            i = j;
        }
        return (int)ans;
    }
}
