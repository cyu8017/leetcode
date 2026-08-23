// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

public class Solution {
    public string AddBinary(string a, string b) {
        int i = a.Length - 1;
        int j = b.Length - 1;
        int carry = 0;
        var result = new System.Text.StringBuilder();

        while (i >= 0 || j >= 0 || carry != 0) {
            int total = carry;
            if (i >= 0) {
                total += a[i] - '0';
                i--;
            }
            if (j >= 0) {
                total += b[j] - '0';
                j--;
            }
            result.Append(total % 2);
            carry = total / 2;
        }

        var chars = result.ToString().ToCharArray();
        System.Array.Reverse(chars);
        return new string(chars);
    }
}
