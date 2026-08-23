// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int[] OccurrencesOfElement(int[] nums, int[] queries, int x) {
        var ids = new List<int>();
        for (int i = 0; i < nums.Length; i++) if (nums[i] == x) ids.Add(i);
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int i = queries[qi];
            if (i - 1 < ids.Count) ans[qi] = ids[i - 1];
            else ans[qi] = -1;
        }
        return ans;
    }
}
