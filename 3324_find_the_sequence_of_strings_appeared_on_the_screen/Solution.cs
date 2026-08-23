// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> StringSequence(string target) {
        var ans = new List<string>();
        var cur = new StringBuilder();
        foreach (char ch in target) {
            cur.Append('a');
            ans.Add(cur.ToString());
            while (cur[cur.Length - 1] != ch) {
                cur[cur.Length - 1] = (char)(cur[cur.Length - 1] + 1);
                ans.Add(cur.ToString());
            }
        }
        return ans;
    }
}
