// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution {
    public int countHomogenous(String s) {
        final long MOD = 1_000_000_007L;
        long ans = 0;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (j < s.length() && s.charAt(j) == s.charAt(i)) {
                j++;
            }
            long length = j - i;
            ans = (ans + length * (length + 1) / 2) % MOD;
            i = j;
        }
        return (int) ans;
    }
}
