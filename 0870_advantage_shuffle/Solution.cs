// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] AdvantageCount(int[] nums1, int[] nums2) {
        var sorted1 = new List<int>(nums1);
        sorted1.Sort();
        int[] ans = new int[nums1.Length];
        var indexed = new (int val, int i)[nums2.Length];
        for (int i = 0; i < nums2.Length; i++) indexed[i] = (nums2[i], i);
        Array.Sort(indexed, (a, b) => b.val.CompareTo(a.val));
        int lo = 0, hi = sorted1.Count - 1;
        foreach (var (val, i) in indexed) {
            if (sorted1[hi] > val) { ans[i] = sorted1[hi]; hi--; }
            else { ans[i] = sorted1[lo]; lo++; }
        }
        return ans;
    }
}
