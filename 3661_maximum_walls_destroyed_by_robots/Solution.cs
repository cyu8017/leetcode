// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxWalls(int[] robots, int[] distance, int[] walls) {
        int n = robots.Length;
        var arr = new (int first, int second)[n];
        for (int i = 0; i < n; i++) arr[i] = (robots[i], distance[i]);
        Array.Sort(arr, (a, b) => a.first.CompareTo(b.first));
        Array.Sort(walls);
        var f = new Dictionary<(int, int), int>();
        int LowerBound(int[] a, int target) {
            int lo = 0, hi = a.Length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (a[mid] < target) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }
        int Dfs(int i, int j) {
            if (i < 0) return 0;
            var key = (i, j);
            if (f.ContainsKey(key)) return f[key];
            int left = arr[i].first - arr[i].second;
            if (i > 0) left = Math.Max(left, arr[i - 1].first + 1);
            int l = LowerBound(walls, left);
            int r = LowerBound(walls, arr[i].first + 1);
            int ans = Dfs(i - 1, 0) + (r - l);
            int right = arr[i].first + arr[i].second;
            if (i + 1 < n) {
                if (j == 0) right = Math.Min(right, arr[i + 1].first - arr[i + 1].second - 1);
                else right = Math.Min(right, arr[i + 1].first - 1);
            }
            l = LowerBound(walls, arr[i].first);
            r = LowerBound(walls, right + 1);
            ans = Math.Max(ans, Dfs(i - 1, 1) + (r - l));
            return f[key] = ans;
        }
        return Dfs(n - 1, 1);
    }
}
