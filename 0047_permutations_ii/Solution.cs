// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

public class Solution {
    public IList<IList<int>> PermuteUnique(int[] nums) {
        Array.Sort(nums);
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
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
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
