// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

public class Solution {
    public IList<IList<int>> FindSubsequences(int[] nums) {
        HashSet<string> seen = new();
        List<IList<int>> result = new();
        Backtrack(nums, 0, new List<int>(), seen, result);
        result.Sort((left, right) => {
            int limit = Math.Min(left.Count, right.Count);
            for (int index = 0; index < limit; index++) {
                int compare = left[index].CompareTo(right[index]);
                if (compare != 0) {
                    return compare;
                }
            }
            return left.Count.CompareTo(right.Count);
        });
        return result;
    }

    private static void Backtrack(
        int[] nums,
        int start,
        List<int> path,
        HashSet<string> seen,
        List<IList<int>> result
    ) {
        if (path.Count >= 2) {
            string key = string.Join(",", path);
            if (seen.Add(key)) {
                result.Add(new List<int>(path));
            }
        }
        HashSet<int> used = new();
        for (int index = start; index < nums.Length; index++) {
            if (used.Contains(nums[index])) {
                continue;
            }
            if (path.Count > 0 && nums[index] < path[^1]) {
                continue;
            }
            used.Add(nums[index]);
            path.Add(nums[index]);
            Backtrack(nums, index + 1, path, seen, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
