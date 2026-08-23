// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

public class Solution {
    public int[] ApplyOperations(int[] nums) {
        int n = nums.Length;
        for (int i = 0; i + 1 < n; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        int[] ans = new int[n];
        int j = 0;
        foreach (int x in nums) if (x != 0) ans[j++] = x;
        return ans;
    }
}
