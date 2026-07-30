// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> MinAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Array.Sort(slots1, (a, b) => a[0].CompareTo(b[0]));
        Array.Sort(slots2, (a, b) => a[0].CompareTo(b[0]));
        int i = 0, j = 0;
        while (i < slots1.Length && j < slots2.Length) {
            int start = Math.Max(slots1[i][0], slots2[j][0]);
            int end = Math.Min(slots1[i][1], slots2[j][1]);
            if (end - start >= duration) return new int[] { start, start + duration };
            if (slots1[i][1] < slots2[j][1]) i++;
            else j++;
        }
        return new int[0];
    }
}
