// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

public class Solution {
    public int[] TransformArray(int[] nums) {
        for (int i = 0; i < nums.Length; i++) nums[i] %= 2;
        int j = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 0) {
                int t = nums[i]; nums[i] = nums[j]; nums[j] = t;
                j++;
            }
        }
        return nums;
    }
}
