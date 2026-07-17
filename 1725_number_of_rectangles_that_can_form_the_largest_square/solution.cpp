// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countGoodRectangles(std::vector<std::vector<int>>& rectangles) {
        int best = 0;
        int count = 0;
        for (const std::vector<int>& rect : rectangles) {
            int side = std::min(rect[0], rect[1]);
            if (side > best) {
                best = side;
                count = 1;
            } else if (side == best) {
                count++;
            }
        }
        return count;
    }
};
