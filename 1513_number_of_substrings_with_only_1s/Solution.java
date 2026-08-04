// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution {
    private static final int MOD = 1_000_000_007;

    public int numSub(String s) {
        long ans = 0;
        int run = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                run++;
                ans += run;
            } else {
                run = 0;
            }
        }
        return (int) (ans % MOD);
    }
}
