// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

public class Solution {
    public int NumberOfArrays(int[] differences, int lower, int upper) {
        long cur = 0, mn = 0, mx = 0;
        foreach (int d in differences) {
            cur += d;
            mn = Math.Min(mn, cur);
            mx = Math.Max(mx, cur);
        }
        long res = (long)(upper - lower) - (mx - mn) + 1;
        return res < 0 ? 0 : (int)res;
    }
}
