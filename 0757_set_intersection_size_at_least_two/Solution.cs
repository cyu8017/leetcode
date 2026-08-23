// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

using System;

public class Solution {
    public int IntersectionSizeTwo(int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[1] != b[1] ? a[1].CompareTo(b[1]) : a[0].CompareTo(b[0]));
        int size = 0, first = -1, second = -1;
        foreach (var interval in intervals) {
            int left = interval[0], right = interval[1];
            if (left <= first) continue;
            if (left <= second) { size++; first = second; second = right; }
            else { size += 2; first = right - 1; second = right; }
        }
        return size;
    }
}
