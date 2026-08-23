// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

public class Solution {
    public int FillCups(int[] amount) {
        int a = amount[0], b = amount[1], c = amount[2];
        if (a < b) { int t = a; a = b; b = t; }
        if (a < c) { int t = a; a = c; c = t; }
        if (b < c) { int t = b; b = c; c = t; }
        if (a >= b + c) return a;
        return (a + b + c + 1) / 2;
    }
}
