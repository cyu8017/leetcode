// LeetCode 1449 - Form Largest Integer With Digits That Add Up To Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

public class Solution {
    public string LargestNumber(int[] cost, int target) {
        var dp = new string[target + 1];
        dp[0] = "";
        for (int total = 1; total <= target; total++) {
            string best = null;
            for (int digit = 1; digit <= 9; digit++) {
                int price = cost[digit - 1];
                if (total >= price && dp[total - price] != null) {
                    string candidate = digit + dp[total - price];
                    if (best == null || candidate.Length > best.Length ||
                        (candidate.Length == best.Length && string.CompareOrdinal(candidate, best) > 0))
                        best = candidate;
                }
            }
            dp[total] = best;
        }
        return dp[target] ?? "0";
    }
}
