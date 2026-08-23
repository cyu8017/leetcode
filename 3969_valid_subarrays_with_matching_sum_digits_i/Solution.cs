// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

public class Solution {
    public int CountValidSubarrays(int[] nums, int x) {
        int n = nums.Length;
        int ans = 0;
        for (int l = 0; l < n; l++) {
            long s = 0;
            for (int r = l; r < n; r++) {
                s += nums[r];
                if (s % 10 == x) {
                    string t = s.ToString();
                    if (t[0] - '0' == x) ans++;
                }
            }
        }
        return ans;
    }
}
