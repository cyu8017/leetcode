// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

using System;
using System.Collections.Generic;

public class Solution {
    public int SmallestAbsent(int[] nums) {
        var s = new HashSet<int>();
        int sum = 0;
        foreach (int x in nums) {
            s.Add(x);
            sum += x;
        }
        int ans = Math.Max(1, sum / nums.Length + 1);
        while (s.Contains(ans)) ans++;
        return ans;
    }
}
