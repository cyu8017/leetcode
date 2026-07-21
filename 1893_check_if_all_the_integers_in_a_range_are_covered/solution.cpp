// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

#include <vector>

class Solution {
public:
    bool isCovered(std::vector<std::vector<int>>& ranges, int left, int right) {
        std::vector<bool> covered(51, false);
        for (const auto& range : ranges) {
            for (int value = range[0]; value <= range[1]; value++) {
                covered[value] = true;
            }
        }
        for (int value = left; value <= right; value++) {
            if (!covered[value]) {
                return false;
            }
        }
        return true;
    }
};
