// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

public class Solution {
    public IList<IList<int>> CombinationSum3(int k, int n) {
        var result = new List<IList<int>>();
        Backtrack(1, k, n, new List<int>(), result);
        return result;
    }

    private void Backtrack(
        int start,
        int k,
        int remaining,
        List<int> path,
        IList<IList<int>> result
    ) {
        if (path.Count == k) {
            if (remaining == 0) {
                result.Add(new List<int>(path));
            }
            return;
        }
        if (remaining <= 0 || path.Count >= k) {
            return;
        }

        for (int num = start; num <= 9; num++) {
            if (num > remaining) {
                break;
            }
            path.Add(num);
            Backtrack(num + 1, k, remaining - num, path, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
