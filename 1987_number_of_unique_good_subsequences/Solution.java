// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

class Solution {
    public int numberOfUniqueGoodSubsequences(String binary) {
        final int MOD = 1_000_000_007;
        long ends0 = 0, ends1 = 0;
        boolean has0 = false;
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '0') {
                has0 = true;
                ends0 = (ends0 + ends1) % MOD;
            } else {
                ends1 = (ends0 + ends1 + 1) % MOD;
            }
        }
        return (int) ((ends0 + ends1 + (has0 ? 1 : 0)) % MOD);
    }
}
