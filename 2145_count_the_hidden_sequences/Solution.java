// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

class Solution {
    public int numberOfArrays(int[] differences, int lower, int upper) {
        long cur = 0, mn = 0, mx = 0;
        for (int d : differences) {
            cur += d;
            mn = Math.min(mn, cur);
            mx = Math.max(mx, cur);
        }
        long res = (long) (upper - lower) - (mx - mn) + 1;
        return res < 0 ? 0 : (int) res;
    }
}
