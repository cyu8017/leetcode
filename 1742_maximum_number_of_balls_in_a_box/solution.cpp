// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

#include <algorithm>
#include <unordered_map>

class Solution {
public:
    int countBalls(int lowLimit, int highLimit) {
        std::unordered_map<int, int> counts;
        for (int value = lowLimit; value <= highLimit; value++) {
            int box = 0;
            int v = value;
            while (v > 0) {
                box += v % 10;
                v /= 10;
            }
            counts[box]++;
        }
        int maxCount = 0;
        for (const auto& [box, count] : counts) {
            maxCount = std::max(maxCount, count);
        }
        return maxCount;
    }
};
