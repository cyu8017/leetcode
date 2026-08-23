// LeetCode 0370 - Range Addition
// https://leetcode.com/problems/range-addition/

#include <vector>

class Solution {
public:
    std::vector<int> getModifiedArray(int length, std::vector<std::vector<int>>& updates) {
        std::vector<int> diff(length + 1, 0);

        for (const auto& update : updates) {
            int start = update[0];
            int end = update[1];
            int inc = update[2];
            diff[start] += inc;
            if (end + 1 < static_cast<int>(diff.size())) {
                diff[end + 1] -= inc;
            }
        }

        std::vector<int> result(length, 0);
        int running = 0;
        for (int index = 0; index < length; ++index) {
            running += diff[index];
            result[index] = running;
        }

        return result;
    }
};
