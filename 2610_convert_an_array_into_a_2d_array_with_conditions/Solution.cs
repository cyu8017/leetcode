// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindMatrix(int[] nums) {
        var freq = new Dictionary<int, int>();
        var ans = new List<IList<int>>();
        foreach (int x in nums) {
            int f = freq.GetValueOrDefault(x, 0);
            if (f == ans.Count) ans.Add(new List<int>());
            ans[f].Add(x);
            freq[x] = f + 1;
        }
        return ans;
    }
}
