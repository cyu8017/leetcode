// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

public class Solution {
    public int LongestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, ans = 0;
        for (int right = 0; right < nums.Length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            ans = Math.Max(ans, right - left + 1);
        }
        return ans;
    }
}
