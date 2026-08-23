// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution {
    public String makeSmallestPalindrome(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        for (int i = 0; i < n / 2; i++) {
            char c = (char) Math.min(arr[i], arr[n - 1 - i]);
            arr[i] = arr[n - 1 - i] = c;
        }
        return new String(arr);
    }
}
