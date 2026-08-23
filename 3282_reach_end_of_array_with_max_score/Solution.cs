// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

public class Solution {
    public long FindMaximumScore(int[] nums) {
        long ans = 0;
        int maxV = 0;
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i] > maxV) maxV = nums[i];
            ans += maxV;
        }
        return ans;
    }
}
