// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

using System;

public class Solution {
    public long MaxRatings(int[][] units) {
        int n = units[0].Length;
        if (n == 1) {
            long ans = 0;
            foreach (var x in units) ans += x[0];
            return ans;
        }
        long answer = 0;
        int mn = int.MaxValue, mn2 = int.MaxValue;
        foreach (var x in units) {
            Array.Sort(x);
            answer += x[1];
            mn2 = Math.Min(mn2, x[1]);
            mn = Math.Min(mn, x[0]);
        }
        return answer - (mn2 - mn);
    }
}
