// LeetCode 1449 - Form Largest Integer With Digits That Add Up To Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

class Solution {
    public String largestNumber(int[] cost, int target) {
        String[] dp = new String[target + 1];
        dp[0] = "";
        for (int total = 1; total <= target; total++) {
            String best = null;
            for (int digit = 1; digit <= 9; digit++) {
                int price = cost[digit - 1];
                if (total >= price && dp[total - price] != null) {
                    String candidate = digit + dp[total - price];
                    if (best == null
                            || candidate.length() > best.length()
                            || (candidate.length() == best.length() && candidate.compareTo(best) > 0)) {
                        best = candidate;
                    }
                }
            }
            dp[total] = best;
        }
        return dp[target] == null ? "0" : dp[target];
    }
}
