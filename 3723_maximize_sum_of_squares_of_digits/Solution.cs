// LeetCode 3723 - Maximize Sum of Squares of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

using System.Text;

public class Solution {
    public string MaxSumOfSquares(int num, int sum) {
        if (num * 9 < sum) return "";
        int k = sum / 9, s = sum % 9;
        var sb = new StringBuilder();
        sb.Append('9', k);
        if (s > 0) sb.Append((char)('0' + s));
        if (sb.Length < num) sb.Append('0', num - sb.Length);
        return sb.ToString();
    }
}
