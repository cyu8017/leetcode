// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

public class Solution {
    public int LengthOfLastWord(string s) {
        int length = 0;
        int i = s.Length - 1;

        while (i >= 0 && s[i] == ' ') {
            i--;
        }

        while (i >= 0 && s[i] != ' ') {
            length++;
            i--;
        }

        return length;
    }
}
