// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

#include <vector>

class Solution {
public:
    int missingNumber(std::vector<int>& arr) {
        int difference = (arr.back() - arr.front()) / static_cast<int>(arr.size());
        for (int i = 1; i < static_cast<int>(arr.size()); ++i) {
            int expected = arr[0] + i * difference;
            if (arr[i] != expected) {
                return expected;
            }
        }
        return arr[0];
    }
};
