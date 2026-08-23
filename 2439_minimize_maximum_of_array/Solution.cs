// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

public class Solution {
    public int MinimizeArrayValue(int[] nums) {
        long sum = 0;
        int ans = 0;
        for (int i = 0; i < nums.Length; i++) {
            sum += nums[i];
            int avg = (int)((sum + i) / (i + 1));
            if (avg > ans) ans = avg;
        }
        return ans;
    }
}
