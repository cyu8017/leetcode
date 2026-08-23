// LeetCode 0046 - Permutations
// https://leetcode.com/problems/permutations/

public class Solution {
    public IList<IList<int>> Permute(int[] nums) {
        var result = new List<IList<int>>();
        var path = new List<int>();
        var used = new bool[nums.Length];
        Backtrack(nums, path, used, result);
        return result;
    }

    private void Backtrack(int[] nums, List<int> path, bool[] used, IList<IList<int>> result) {
        if (path.Count == nums.Length) {
            result.Add(new List<int>(path));
            return;
        }

        for (int i = 0; i < nums.Length; i++) {
            if (used[i]) {
                continue;
            }
            used[i] = true;
            path.Add(nums[i]);
            Backtrack(nums, path, used, result);
            path.RemoveAt(path.Count - 1);
            used[i] = false;
        }
    }
}
