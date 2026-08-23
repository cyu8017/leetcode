// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

using System.Collections.Generic;

public class Solution {
    public int FindMaxK(int[] nums) {
        var seen = new HashSet<int>();
        int ans = -1;
        foreach (int x in nums) {
            seen.Add(x);
            if (x > 0 && seen.Contains(-x) && x > ans) ans = x;
            if (x < 0 && seen.Contains(-x) && -x > ans) ans = -x;
        }
        return ans;
    }
}
