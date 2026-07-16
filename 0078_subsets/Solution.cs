// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

public class Solution {
    public IList<IList<int>> Subsets(int[] nums) {
        var result = new List<IList<int>> { new List<int>() };

        foreach (int num in nums) {
            int size = result.Count;
            for (int i = 0; i < size; i++) {
                var subset = new List<int>(result[i]) { num };
                result.Add(subset);
            }
        }

        return result;
    }
}
