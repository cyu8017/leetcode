// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

using System;
using System.Collections.Generic;

public class Solution {
    int Lis(List<int> a) {
        var tails = new List<int>();
        foreach (int x in a) {
            int lo = 0, hi = tails.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (tails[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            if (lo == tails.Count) tails.Add(x);
            else tails[lo] = x;
        }
        return tails.Count;
    }

    public int MaxPathLength(int[][] coordinates, int k) {
        int n = coordinates.Length;
        var arr = new (int x, int y, int i)[n];
        for (int i = 0; i < n; i++) arr[i] = (coordinates[i][0], coordinates[i][1], i);
        Array.Sort(arr, (a, b) => {
            if (a.x == b.x) return b.y.CompareTo(a.y);
            return a.x.CompareTo(b.x);
        });
        int kx = coordinates[k][0], ky = coordinates[k][1];
        var left = new List<int>();
        var right = new List<int>();
        foreach (var p in arr) {
            if (p.x < kx && p.y < ky) left.Add(p.y);
            if (p.x > kx && p.y > ky) right.Add(p.y);
        }
        return Lis(left) + 1 + Lis(right);
    }
}
