// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

public class Solution {
    public bool CanPermutePalindrome(string s) {
        int[] counts = new int[26];
        foreach (char ch in s) {
            counts[ch - 'a']++;
        }
        int odd = 0;
        foreach (int count in counts) {
            if (count % 2 != 0) {
                odd++;
            }
        }
        return odd <= 1;
    }
}
