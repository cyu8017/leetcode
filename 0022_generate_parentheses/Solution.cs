// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        var result = new List<string>();
        Backtrack(n, new List<char>(), 0, 0, result);
        return result;
    }

    private void Backtrack(int n, List<char> path, int openCount, int closeCount, IList<string> result) {
        if (path.Count == 2 * n) {
            result.Add(new string(path.ToArray()));
            return;
        }
        if (openCount < n) {
            path.Add('(');
            Backtrack(n, path, openCount + 1, closeCount, result);
            path.RemoveAt(path.Count - 1);
        }
        if (closeCount < openCount) {
            path.Add(')');
            Backtrack(n, path, openCount, closeCount + 1, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
