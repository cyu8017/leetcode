// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

public class Solution {
    public string ReversePrefix(string word, char ch) {
        int pos = word.IndexOf(ch);
        if (pos < 0) return word;
        char[] arr = word.ToCharArray();
        System.Array.Reverse(arr, 0, pos + 1);
        return new string(arr);
    }
}
