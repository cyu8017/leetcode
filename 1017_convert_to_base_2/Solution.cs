// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

using System.Text;

public class Solution {
    public string BaseNeg2(int n) {
        if (n == 0) return "0";
        var ans = new StringBuilder();
        while (n != 0) {
            int rem = n % -2;
            n /= -2;
            if (rem < 0) {
                n++;
                rem += 2;
            }
            ans.Append(rem);
        }
        var chars = ans.ToString().ToCharArray();
        Array.Reverse(chars);
        return new string(chars);
    }
}
