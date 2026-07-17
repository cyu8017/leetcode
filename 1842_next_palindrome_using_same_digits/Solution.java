// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

class Solution {
    public String nextPalindrome(String num) {
        char[] nums = num.toCharArray();
        if (!nextPermutation(nums)) {
            return "";
        }

        int n = nums.length;
        for (int i = 0; i < n / 2; i++) {
            nums[n - i - 1] = nums[i];
        }
        return new String(nums);
    }

    private boolean nextPermutation(char[] nums) {
        int n = nums.length / 2;
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i < 0) {
            return false;
        }

        int j = n - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        swap(nums, i, j);

        int left = i + 1;
        int right = n - 1;
        while (left < right) {
            swap(nums, left, right);
            left++;
            right--;
        }
        return true;
    }

    private void swap(char[] nums, int i, int j) {
        char temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
