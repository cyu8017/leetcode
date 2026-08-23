// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumSetSize(int[] nums1, int[] nums2) {
        var s1 = new HashSet<int>(nums1);
        var s2 = new HashSet<int>(nums2);
        int a = 0, b = 0, c = 0;
        foreach (int x in s1) if (!s2.Contains(x)) a++;
        foreach (int x in s2) {
            if (!s1.Contains(x)) b++;
            else c++;
        }
        int n = nums1.Length;
        a = Math.Min(a, n / 2);
        b = Math.Min(b, n / 2);
        return Math.Min(a + b + c, n);
    }
}
