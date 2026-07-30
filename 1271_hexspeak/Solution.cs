// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

public class Solution {
    public string ToHexspeak(string num) {
        long value = long.Parse(num);
        const string digits = "0123456789ABCDEF";
        var outChars = new System.Text.StringBuilder();
        while (value > 0) {
            int rem = (int)(value % 16);
            if (rem >= 2 && rem <= 9) return "ERROR";
            outChars.Insert(0, digits[rem]);
            value /= 16;
        }
        string result = outChars.Length == 0 ? "0" : outChars.ToString();
        return result.Replace('0', 'O').Replace('1', 'I');
    }
}
