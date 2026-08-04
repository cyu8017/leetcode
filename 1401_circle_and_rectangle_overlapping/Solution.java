// LeetCode 1401 - Circle And Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int x = Math.min(Math.max(xCenter, x1), x2);
        int y = Math.min(Math.max(yCenter, y1), y2);
        return (long)(x - xCenter) * (x - xCenter) + (long)(y - yCenter) * (y - yCenter) <= (long)radius * radius;
    }
}
