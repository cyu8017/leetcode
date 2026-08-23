// LeetCode 0031 - Next Permutation
// https://leetcode.com/problems/next-permutation/

public class Solution {
    public void NextPermutation(int[] nums) {
        int i = nums.Length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            int j = nums.Length - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            (nums[i], nums[j]) = (nums[j], nums[i]);
        }

        int left = i + 1;
        int right = nums.Length - 1;
        while (left < right) {
            (nums[left], nums[right]) = (nums[right], nums[left]);
            left++;
            right--;
        }
    }
}
