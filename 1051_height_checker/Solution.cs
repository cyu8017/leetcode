// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

using System;
using System.Linq;

public class Solution {
    public int HeightChecker(int[] heights) {
        int[] expected = (int[])heights.Clone();
        Array.Sort(expected);
        int ans = 0;
        for (int i = 0; i < heights.Length; i++) {
            if (heights[i] != expected[i]) {
                ans++;
            }
        }
        return ans;
    }
}
