// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

class Solution {
    public int[] constructRectangle(int area) {
        int limit = (int) Math.sqrt(area);
        for (int width = limit; width > 0; width--) {
            if (area % width == 0) {
                return new int[] { area / width, width };
            }
        }
        return new int[] { area, 1 };
    }
}
