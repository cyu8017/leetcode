// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

public class Solution {
    public string ReplaceDigits(string s) {
        char[] chars = s.ToCharArray();
        for (int i = 1; i < chars.Length; i += 2) {
            chars[i] = (char)(chars[i - 1] + (chars[i] - '0'));
        }
        return new string(chars);
    }
}
