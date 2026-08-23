// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

using System;

public class Solution {
    public int MaxDistToClosest(int[] seats) {
        int n = seats.Length, prev = -1, ans = 0;
        for (int i = 0; i < n; i++) {
            if (seats[i] != 0) {
                if (prev == -1) ans = i;
                else ans = Math.Max(ans, (i - prev) / 2);
                prev = i;
            }
        }
        ans = Math.Max(ans, n - 1 - prev);
        return ans;
    }
}
