// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

public class Solution {
    public long[] ResultArray(int[] nums, int k) {
        long[] ans = new long[k], dp = new long[k];
        foreach (int num in nums) {
            long[] newDp = new long[k];
            int nm = num % k;
            newDp[nm] = 1;
            for (int i = 0; i < k; i++) newDp[(i * nm) % k] += dp[i];
            for (int i = 0; i < k; i++) ans[i] += newDp[i];
            dp = newDp;
        }
        return ans;
    }
}
