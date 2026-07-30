// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

using System.Collections.Generic;

public class Solution {
    public int[] LongestObstacleCourseAtEachPosition(int[] obstacles) {
        var tails = new List<int>();
        var ans = new int[obstacles.Length];
        for (int idx = 0; idx < obstacles.Length; idx++) {
            int x = obstacles[idx];
            int i = UpperBound(tails, x);
            if (i == tails.Count) tails.Add(x);
            else tails[i] = x;
            ans[idx] = i + 1;
        }
        return ans;
    }

    int UpperBound(List<int> a, int x) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}