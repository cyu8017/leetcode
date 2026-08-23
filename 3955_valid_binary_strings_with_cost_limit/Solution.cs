// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> GenerateValidStrings(int n, int k) {
        var ans = new List<string>();
        var path = new StringBuilder(n);
        void Dfs(int i, int tot) {
            if (i >= n) {
                ans.Add(path.ToString());
                return;
            }
            path.Append('0');
            Dfs(i + 1, tot);
            path.Length--;
            if ((path.Length == 0 || path[path.Length - 1] == '0') && tot + i <= k) {
                path.Append('1');
                Dfs(i + 1, tot + i);
                path.Length--;
            }
        }
        Dfs(0, 0);
        return ans;
    }
}
