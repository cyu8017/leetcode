// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

public class Solution {
    public int MaxArea(int[] height) {
        int left = 0;
        int right = height.Length - 1;
        int best = 0;

        while (left < right) {
            int width = right - left;
            best = Math.Max(best, Math.Min(height[left], height[right]) * width);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return best;
    }
}
