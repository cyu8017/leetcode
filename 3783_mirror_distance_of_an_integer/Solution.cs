// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

using System;

public class Solution {
    public int MirrorDistance(int n) {
        int Reverse(int x) {
            int y = 0;
            for (; x > 0; x /= 10) y = y * 10 + x % 10;
            return y;
        }
        return Math.Abs(n - Reverse(n));
    }
}
