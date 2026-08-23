// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

using System.Collections.Generic;
using System.Text;

public class Solution {
    private readonly Dictionary<string, List<char>> transitions = new Dictionary<string, List<char>>();
    private readonly Dictionary<string, bool> memo = new Dictionary<string, bool>();

    public bool PyramidTransition(string bottom, IList<string> allowed) {
        transitions.Clear();
        memo.Clear();
        foreach (string triple in allowed) {
            string key = triple.Substring(0, 2);
            if (!transitions.ContainsKey(key)) transitions[key] = new List<char>();
            transitions[key].Add(triple[2]);
        }
        return Dfs(bottom);
    }

    private bool Dfs(string row) {
        if (row.Length == 1) return true;
        if (memo.TryGetValue(row, out bool cached)) return cached;
        var options = new List<List<char>>();
        for (int i = 0; i + 1 < row.Length; i++) {
            string key = row.Substring(i, 2);
            if (!transitions.ContainsKey(key)) return memo[row] = false;
            options.Add(transitions[key]);
        }
        var path = new StringBuilder();
        return memo[row] = Build(0, options, path);
    }

    private bool Build(int index, List<List<char>> options, StringBuilder path) {
        if (index == options.Count) return Dfs(path.ToString());
        foreach (char ch in options[index]) {
            path.Append(ch);
            if (Build(index + 1, options, path)) return true;
            path.Length--;
        }
        return false;
    }
}
