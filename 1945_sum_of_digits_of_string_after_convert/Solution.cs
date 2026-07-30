// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

using System.Linq;
using System.Text;

public class Solution {
    public int GetLucky(string s, int k) {
        var sb = new StringBuilder();
        foreach (char c in s) sb.Append(c - 'a' + 1);
        string num = sb.ToString();
        for (int i = 0; i < k; i++)
            num = num.Sum(d => d - '0').ToString();
        return int.Parse(num);
    }
}