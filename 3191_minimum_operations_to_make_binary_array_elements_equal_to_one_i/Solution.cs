// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

public class Solution {
    public int MinOperations(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 0) {
                if (i + 2 >= nums.Length) return -1;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                ans++;
            }
        }
        return ans;
    }
}
