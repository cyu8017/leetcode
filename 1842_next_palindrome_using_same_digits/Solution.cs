// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

public class Solution {
    public string NextPalindrome(string num) {
        char[] chars = num.ToCharArray();
        if (!NextPermutation(chars)) return "";
        int n = chars.Length;
        for (int i = 0; i < n / 2; i++) chars[n - i - 1] = chars[i];
        return new string(chars);
    }

    private bool NextPermutation(char[] nums) {
        int half = nums.Length / 2;
        int i = half - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) i--;
        if (i < 0) return false;
        int j = half - 1;
        while (nums[j] <= nums[i]) j--;
        (nums[i], nums[j]) = (nums[j], nums[i]);
        System.Array.Reverse(nums, i + 1, half - i - 1);
        return true;
    }
}
