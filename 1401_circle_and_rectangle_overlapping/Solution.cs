// LeetCode 1401 - Circle And Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

public class Solution {
    public bool CheckOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int x = System.Math.Min(System.Math.Max(xCenter, x1), x2);
        int y = System.Math.Min(System.Math.Max(yCenter, y1), y2);
        return (long)(x - xCenter) * (x - xCenter) + (long)(y - yCenter) * (y - yCenter) <= (long)radius * radius;
    }
}
