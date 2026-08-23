// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

public class Solution {
    public long NumberOfSubsequences(int[] nums) {
        int n = nums.Length;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 2; j < n; j++) {
                for (int k = j + 2; k < n; k++) {
                    for (int l = k + 2; l < n; l++) {
                        if ((long)nums[i] * nums[k] == (long)nums[j] * nums[l]) ans++;
                    }
                }
            }
        }
        return ans;
    }
}
