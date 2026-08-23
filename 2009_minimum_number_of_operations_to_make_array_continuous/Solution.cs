// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

using System;
using System.Linq;

public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        var uniq = nums.Distinct().OrderBy(x => x).ToArray();
        int ans = n, j = 0;
        for (int i = 0; i < uniq.Length; i++) {
            while (j < uniq.Length && uniq[j] - uniq[i] + 1 <= n) j++;
            ans = Math.Min(ans, n - (j - i));
        }
        return ans;
    }
}
