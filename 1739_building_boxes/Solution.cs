// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

public class Solution {
    public int MinimumBoxes(int n) {
        long height = 0;
        long used = 0;
        long baseCount = 0;
        while (used + (height + 1) * (height + 2) / 2 <= n) {
            height++;
            long layer = height * (height + 1) / 2;
            used += layer;
            baseCount += height;
        }
        long extra = 0;
        while (used < n) {
            extra++;
            used += extra;
        }
        return (int)(baseCount + extra);
    }
}
