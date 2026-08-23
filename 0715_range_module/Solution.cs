// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

using System;
using System.Collections.Generic;

public class RangeModule {
    private List<(int start, int end)> intervals = new List<(int, int)>();
    public RangeModule() { }

    public void AddRange(int left, int right) {
        var next = new List<(int, int)>();
        bool placed = false;
        foreach (var (start, end) in intervals) {
            if (end < left) next.Add((start, end));
            else if (right < start) {
                if (!placed) { next.Add((left, right)); placed = true; }
                next.Add((start, end));
            } else {
                left = Math.Min(left, start);
                right = Math.Max(right, end);
            }
        }
        if (!placed) next.Add((left, right));
        intervals = next;
    }

    public bool QueryRange(int left, int right) {
        foreach (var (start, end) in intervals) {
            if (start <= left && right <= end) return true;
            if (end >= right) break;
        }
        return false;
    }

    public void RemoveRange(int left, int right) {
        var next = new List<(int, int)>();
        foreach (var (start, end) in intervals) {
            if (end <= left || right <= start) next.Add((start, end));
            else {
                if (start < left) next.Add((start, left));
                if (right < end) next.Add((right, end));
            }
        }
        intervals = next;
    }
}
