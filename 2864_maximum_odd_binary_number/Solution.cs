// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

using System.Text;

public class Solution {
    public string MaximumOddBinaryNumber(string s) {
        int ones = 0;
        foreach (char c in s) if (c == '1') ones++;
        int zeros = s.Length - ones;
        var b = new StringBuilder(s.Length);
        for (int i = 0; i < ones - 1; i++) b.Append('1');
        for (int i = 0; i < zeros; i++) b.Append('0');
        b.Append('1');
        return b.ToString();
    }
}
