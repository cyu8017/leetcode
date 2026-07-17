// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution {
    public int minimumLength(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right && s.charAt(left) == s.charAt(right)) {
            char ch = s.charAt(left);
            while (left <= right && s.charAt(left) == ch) {
                left++;
            }
            while (left <= right && s.charAt(right) == ch) {
                right--;
            }
        }
        return right - left + 1;
    }
}
