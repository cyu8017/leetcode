// LeetCode 3038 - Maximum Number of Operations With the Same Score I
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

public class Solution {
    public int MaxOperations(int[] nums) {
        int s = nums[0] + nums[1], n = nums.Length, ans = 0;
        for (int i = 0; i + 1 < n && nums[i] + nums[i + 1] == s; i += 2) ans++;
        return ans;
    }
}
