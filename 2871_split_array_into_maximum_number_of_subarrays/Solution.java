// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

class Solution {
    public int maxSubarrays(int[] nums) {
        int ans = 0, cur = -1;
        for (int v : nums) {
            if (cur == -1) cur = v;
            else cur &= v;
            if (cur == 0) {
                ans++;
                cur = -1;
            }
        }
        return ans == 0 ? 1 : ans;
    }
}
