// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

using System.Text;

public class Solution {
    public string StringHash(string s, int k) {
        var outSb = new StringBuilder(s.Length / k);
        for (int i = 0; i < s.Length; i += k) {
            int sum = 0;
            for (int j = i; j < i + k; j++) sum += s[j] - 'a';
            outSb.Append((char)('a' + sum % 26));
        }
        return outSb.ToString();
    }
}
