// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

class Solution {
    public int minimumBoxes(int n) {
        long height = 0;
        long used = 0;
        long base = 0;
        while (used + (height + 1) * (height + 2) / 2 <= n) {
            height++;
            long layer = height * (height + 1) / 2;
            used += layer;
            base += height;
        }
        long extra = 0;
        while (used < n) {
            extra++;
            used += extra;
        }
        return (int) (base + extra);
    }
}
