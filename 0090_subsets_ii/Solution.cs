// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

public class Solution {
    public IList<IList<int>> SubsetsWithDup(int[] nums) {
        Array.Sort(nums);
        var result = new List<IList<int>>();
        Backtrack(nums, 0, new List<int>(), result);
        return result;
    }

    private void Backtrack(int[] nums, int start, List<int> path, IList<IList<int>> result) {
        result.Add(new List<int>(path));
        for (int i = start; i < nums.Length; i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            path.Add(nums[i]);
            Backtrack(nums, i + 1, path, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
