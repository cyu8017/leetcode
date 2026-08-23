// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

public class Solution {
    public int[] ResultsArray(int[] nums, int k) {
        int n = nums.Length;
        int[] ans = new int[n - k + 1];
        for (int i = 0; i <= n - k; i++) {
            bool ok = true;
            for (int j = i + 1; j < i + k; j++) {
                if (nums[j] != nums[j - 1] + 1) { ok = false; break; }
            }
            ans[i] = ok ? nums[i + k - 1] : -1;
        }
        return ans;
    }
}
