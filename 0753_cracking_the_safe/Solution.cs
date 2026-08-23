// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

using System.Collections.Generic;
using System.Text;

public class Solution {
    private readonly HashSet<string> seen = new HashSet<string>();
    private readonly List<char> path = new List<char>();

    public string CrackSafe(int n, int k) {
        seen.Clear();
        path.Clear();
        string start = new string('0', n - 1);
        Dfs(start, k);
        var result = new StringBuilder();
        foreach (char ch in path) result.Append(ch);
        return result.ToString() + start;
    }

    private void Dfs(string node, int k) {
        for (int d = 0; d < k; d++) {
            char digit = (char)('0' + d);
            string edge = node + digit;
            if (seen.Add(edge)) {
                Dfs(edge.Substring(1), k);
                path.Add(digit);
            }
        }
    }
}
