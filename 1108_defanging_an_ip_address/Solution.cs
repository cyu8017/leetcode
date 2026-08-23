// LeetCode 1108 - Defanging an IP Address
// https://leetcode.com/problems/defanging-an-ip-address/

using System.Text;

public class Solution {
    public string DefangIPaddr(string address) {
        var ans = new StringBuilder();
        foreach (char ch in address) {
            if (ch == '.') {
                ans.Append("[.]");
            } else {
                ans.Append(ch);
            }
        }
        return ans.ToString();
    }
}
