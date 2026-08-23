// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

public class Solution {
    public int MaxSubarrays(int[] nums) {
        int ans = 0, cur = -1;
        foreach (int v in nums) {
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
