// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

using System.Text;

public class Solution {
    public string StrWithout3a3b(int a, int b) {
        var ans = new StringBuilder();
        while (a > 0 || b > 0) {
            bool writeA;
            if (ans.Length >= 2 && ans[ans.Length - 1] == ans[ans.Length - 2])
                writeA = ans[ans.Length - 1] == 'b';
            else
                writeA = a >= b;
            if (writeA) { ans.Append('a'); a--; }
            else { ans.Append('b'); b--; }
        }
        return ans.ToString();
    }
}
