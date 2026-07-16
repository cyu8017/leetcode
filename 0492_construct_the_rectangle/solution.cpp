// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<int> constructRectangle(int area) {
        const int limit = static_cast<int>(std::sqrt(area));
        for (int width = limit; width > 0; --width) {
            if (area % width == 0) {
                return {area / width, width};
            }
        }
        return {area, 1};
    }
};
