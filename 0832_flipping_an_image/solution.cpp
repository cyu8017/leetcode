// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> flipAndInvertImage(std::vector<std::vector<int>>& image) {
        for (auto& row : image) {
            std::reverse(row.begin(), row.end());
            for (int& x : row) {
                x = 1 - x;
            }
        }
        return image;
    }
};
