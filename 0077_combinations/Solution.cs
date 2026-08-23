// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

public class Solution {
    public IList<IList<int>> Combine(int n, int k) {
        var result = new List<IList<int>>();
        var path = new List<int>();
        Backtrack(n, k, 1, path, result);
        return result;
    }

    private void Backtrack(int n, int k, int start, List<int> path, IList<IList<int>> result) {
        if (path.Count == k) {
            result.Add(new List<int>(path));
            return;
        }

        int remaining = k - path.Count;
        for (int i = start; i <= n - remaining + 1; i++) {
            path.Add(i);
            Backtrack(n, k, i + 1, path, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
