// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

public class Solution {
    public string LicenseKeyFormatting(string s, int k) {
        char[] chars = s.Where(ch => ch != '-').Select(char.ToUpperInvariant).ToArray();
        if (chars.Length == 0) {
            return "";
        }
        int firstLen = chars.Length % k;
        if (firstLen == 0) {
            firstLen = k;
        }
        List<string> parts = new() { new string(chars, 0, firstLen) };
        for (int i = firstLen; i < chars.Length; i += k) {
            parts.Add(new string(chars, i, k));
        }
        return string.Join("-", parts);
    }
}
