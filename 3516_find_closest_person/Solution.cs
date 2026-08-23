// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

using System;

public class Solution {
    public int FindClosest(int x, int y, int z) {
        int a = Math.Abs(x - z), b = Math.Abs(y - z);
        if (a == b) return 0;
        return a < b ? 1 : 2;
    }
}
