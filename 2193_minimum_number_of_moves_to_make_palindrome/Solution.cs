// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

public class Solution {
    public int MinMovesToMakePalindrome(string s) {
        var b = new System.Text.StringBuilder(s);
        int ans = 0;
        while (b.Length > 1) {
            int j = b.Length - 1;
            while (j > 0 && b[j] != b[0]) j--;
            if (j == 0) {
                ans += b.Length / 2;
                b.Remove(0, 1);
                continue;
            }
            ans += b.Length - 1 - j;
            b.Remove(j, 1);
            b.Remove(0, 1);
        }
        return ans;
    }
}
