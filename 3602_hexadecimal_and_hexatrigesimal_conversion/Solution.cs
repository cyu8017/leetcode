// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

using System.Text;

public class Solution {
    string F(int x, int k) {
        var res = new StringBuilder();
        while (x > 0) {
            int v = x % k;
            res.Append(v <= 9 ? (char)('0' + v) : (char)('A' + v - 10));
            x /= k;
        }
        var arr = res.ToString().ToCharArray();
        System.Array.Reverse(arr);
        return new string(arr);
    }
    public string ConcatHex36(int n) {
        return F(n * n, 16) + F(n * n * n, 36);
    }
}
