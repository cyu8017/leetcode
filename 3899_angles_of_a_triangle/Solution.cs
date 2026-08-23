// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

using System;

public class Solution {
    public double[] InternalAngles(int[] sides) {
        Array.Sort(sides);
        int a = sides[0], b = sides[1], c = sides[2];
        if (a + b <= c) return new double[0];
        double PI = Math.Acos(-1.0);
        double A = Math.Acos((double)(b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / PI;
        double B = Math.Acos((double)(a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / PI;
        double C = 180.0 - A - B;
        return new double[] { A, B, C };
    }
}
