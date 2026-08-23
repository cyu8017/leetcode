// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

public class Solution {
    public IList<IList<int>> GetFactors(int n) {
        var result = new List<IList<int>>();
        Backtrack(n, 2, new List<int>(), result);
        return result;
    }

    private void Backtrack(int remain, int start, List<int> path, IList<IList<int>> result) {
        if (start > remain) {
            if (path.Count > 1) {
                result.Add(new List<int>(path));
            }
            return;
        }

        for (int factor = start; factor * factor <= remain; factor++) {
            if (remain % factor == 0) {
                path.Add(factor);
                Backtrack(remain / factor, factor, path, result);
                path.RemoveAt(path.Count - 1);
            }
        }

        if (path.Count > 0) {
            path.Add(remain);
            if (path.Count > 1) {
                result.Add(new List<int>(path));
            }
            path.RemoveAt(path.Count - 1);
        }
    }
}
