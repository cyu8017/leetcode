// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

import java.util.Arrays;

class Solution {
    public double[] internalAngles(int[] sides) {
        Arrays.sort(sides);
        int a = sides[0], b = sides[1], c = sides[2];
        if (a + b <= c) return new double[0];
        double PI = Math.acos(-1.0);
        double A = Math.acos((double) (b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / PI;
        double B = Math.acos((double) (a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / PI;
        double C = 180.0 - A - B;
        return new double[] { A, B, C };
    }
}
