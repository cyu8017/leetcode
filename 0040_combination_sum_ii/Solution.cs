// LeetCode 0040 - Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/

public class Solution {
    public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
        Array.Sort(candidates);
        var result = new List<IList<int>>();
        Backtrack(candidates, target, new List<int>(), 0, result);
        return result;
    }

    private void Backtrack(int[] candidates, int remaining, List<int> path, int start, IList<IList<int>> result) {
        if (remaining == 0) {
            result.Add(new List<int>(path));
            return;
        }
        if (remaining < 0) {
            return;
        }

        for (int i = start; i < candidates.Length; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            path.Add(candidates[i]);
            Backtrack(candidates, remaining - candidates[i], path, i + 1, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
