// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

#include <vector>

class Vector2D {
    const std::vector<std::vector<int>>& vec;
    int row = 0;
    int col = 0;

    void advance() {
        while (row < static_cast<int>(vec.size()) && col >= static_cast<int>(vec[row].size())) {
            row += 1;
            col = 0;
        }
    }

public:
    Vector2D(const std::vector<std::vector<int>>& vec) : vec(vec) {
        advance();
    }

    int next() {
        int value = vec[row][col];
        col += 1;
        advance();
        return value;
    }

    bool hasNext() {
        advance();
        return row < static_cast<int>(vec.size());
    }
};
