// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

class Solution {
    public int countValidSubarrays(int[] nums, int x) {
        int n = nums.length;
        int ans = 0;
        for (int l = 0; l < n; l++) {
            long s = 0;
            for (int r = l; r < n; r++) {
                s += nums[r];
                if (s % 10 == x) {
                    String t = Long.toString(s);
                    if (t.charAt(0) - '0' == x) ans++;
                }
            }
        }
        return ans;
    }
}
