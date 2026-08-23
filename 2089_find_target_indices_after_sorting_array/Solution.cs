// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

public class Solution {
    public IList<int> TargetIndices(int[] nums, int target) {
        int less = 0, eq = 0;
        foreach (int x in nums) {
            if (x < target) less++;
            else if (x == target) eq++;
        }
        var ans = new List<int>(eq);
        for (int i = 0; i < eq; i++) ans.Add(less + i);
        return ans;
    }
}
