// LeetCode 0039 - Combination Sum
// https://leetcode.com/problems/combination-sum/

public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
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
            path.Add(candidates[i]);
            Backtrack(candidates, remaining - candidates[i], path, i, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
