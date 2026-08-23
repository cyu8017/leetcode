// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

class Solution {
public:
    int minimumBoxes(int n) {
        long long height = 0;
        long long used = 0;
        long long base = 0;
        while (used + (height + 1) * (height + 2) / 2 <= n) {
            height++;
            long long layer = height * (height + 1) / 2;
            used += layer;
            base += height;
        }
        long long extra = 0;
        while (used < n) {
            extra++;
            used += extra;
        }
        return static_cast<int>(base + extra);
    }
};
