// LeetCode 0455 - Assign Cookies
// https://leetcode.com/problems/assign-cookies/

using System;

public class Solution {
    public int FindContentChildren(int[] g, int[] s) {
        Array.Sort(g);
        Array.Sort(s);
        int child = 0;
        int cookie = 0;
        while (child < g.Length && cookie < s.Length) {
            if (s[cookie] >= g[child]) {
                child++;
            }
            cookie++;
        }
        return child;
    }
}
