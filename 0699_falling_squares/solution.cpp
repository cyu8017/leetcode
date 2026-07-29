// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

#include <algorithm>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<int> fallingSquares(std::vector<std::vector<int>>& positions) {
        std::vector<std::tuple<int, int, int>> intervals;
        std::vector<int> answer;
        int maxHeight = 0;
        for (const auto& pos : positions) {
            const int left = pos[0];
            const int side = pos[1];
            const int right = left + side;
            int base = 0;
            for (const auto& [l, r, height] : intervals) {
                if (r > left && l < right) {
                    base = std::max(base, height);
                }
            }
            const int height = base + side;
            intervals.emplace_back(left, right, height);
            maxHeight = std::max(maxHeight, height);
            answer.push_back(maxHeight);
        }
        return answer;
    }
};
