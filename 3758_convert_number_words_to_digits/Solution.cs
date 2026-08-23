// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

using System.Text;

public class Solution {
    public string ConvertNumber(string s) {
        string[] d = {
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
        };
        int n = s.Length;
        var ans = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                int m = d[j].Length;
                if (i + m <= n && s.Substring(i, m) == d[j]) {
                    ans.Append((char)('0' + j));
                    i += m - 1;
                    break;
                }
            }
        }
        return ans.ToString();
    }
}
