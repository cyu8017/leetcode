// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

public class Solution {
    public long ZeroFilledSubarray(int[] nums) {
        long ans = 0, streak = 0;
        foreach (int x in nums) {
            if (x == 0) { streak++; ans += streak; }
            else streak = 0;
        }
        return ans;
    }
}
