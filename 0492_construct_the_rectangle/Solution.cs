// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

public class Solution {
    public int[] ConstructRectangle(int area) {
        int limit = (int)Math.Sqrt(area);
        for (int width = limit; width > 0; width--) {
            if (area % width == 0) {
                return new[] { area / width, width };
            }
        }
        return new[] { area, 1 };
    }
}
