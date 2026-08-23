// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

class Solution {
    public int minMovesToMakePalindrome(String s) {
        StringBuilder b = new StringBuilder(s);
        int ans = 0;
        while (b.length() > 1) {
            int j = b.length() - 1;
            while (j > 0 && b.charAt(j) != b.charAt(0)) j--;
            if (j == 0) {
                ans += b.length() / 2;
                b.deleteCharAt(0);
                continue;
            }
            ans += b.length() - 1 - j;
            b.deleteCharAt(j);
            b.deleteCharAt(0);
        }
        return ans;
    }
}
