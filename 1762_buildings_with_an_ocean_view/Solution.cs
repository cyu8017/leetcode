// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

using System.Collections.Generic;

public class Solution {
    public int[] FindBuildings(int[] heights) {
        var ans = new List<int>();
        int tallest = 0;
        for (int i = heights.Length - 1; i >= 0; i--) {
            if (heights[i] > tallest) {
                ans.Add(i);
                tallest = heights[i];
            }
        }
        ans.Reverse();
        return ans.ToArray();
    }
}
