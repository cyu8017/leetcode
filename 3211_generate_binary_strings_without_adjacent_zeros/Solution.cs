// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> ValidStrings(int n) {
        var ans = new List<string>();
        var t = new StringBuilder();
        void Dfs(int i) {
            if (i >= n) { ans.Add(t.ToString()); return; }
            for (int j = 0; j < 2; j++) {
                if ((j == 0 && (i == 0 || t[i - 1] == '1')) || j == 1) {
                    t.Append((char)('0' + j));
                    Dfs(i + 1);
                    t.Length--;
                }
            }
        }
        Dfs(0);
        return ans;
    }
}
