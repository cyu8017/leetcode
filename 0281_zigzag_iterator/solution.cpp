// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

#include <vector>

class ZigzagIterator {
    std::vector<std::vector<int>> vectors;
    std::vector<int> indices;
    int turn = 0;

public:
    ZigzagIterator(const std::vector<int>& v1, const std::vector<int>& v2) {
        vectors = {v1, v2};
        indices = {0, 0};
    }

    int next() {
        while (indices[turn] >= static_cast<int>(vectors[turn].size())) {
            turn = 1 - turn;
        }
        int value = vectors[turn][indices[turn]];
        indices[turn] += 1;
        turn = 1 - turn;
        return value;
    }

    bool hasNext() {
        for (int index = 0; index < static_cast<int>(vectors.size()); index++) {
            if (indices[index] < static_cast<int>(vectors[index].size())) {
                return true;
            }
        }
        return false;
    }
};
