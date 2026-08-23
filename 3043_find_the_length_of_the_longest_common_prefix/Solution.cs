// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestCommonPrefix(int[] arr1, int[] arr2) {
        var s = new HashSet<int>();
        foreach (int x0 in arr1) {
            for (int x = x0; x > 0; x /= 10) s.Add(x);
        }
        int mx = 0;
        foreach (int x0 in arr2) {
            for (int x = x0; x > 0; x /= 10) {
                if (s.Contains(x)) {
                    mx = Math.Max(mx, x);
                    break;
                }
            }
        }
        return mx > 0 ? mx.ToString().Length : 0;
    }
}
