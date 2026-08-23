// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

class Solution {
    public boolean canPermutePalindrome(String s) {
        int[] counts = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counts[s.charAt(i) - 'a']++;
        }
        int odd = 0;
        for (int count : counts) {
            if (count % 2 != 0) {
                odd++;
            }
        }
        return odd <= 1;
    }
}
