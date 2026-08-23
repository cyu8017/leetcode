// LeetCode 0335 - Self Crossing
// https://leetcode.com/problems/self-crossing/

#include <vector>

class Solution {
public:
    bool isSelfCrossing(std::vector<int>& distance) {
        for (int index = 3; index < static_cast<int>(distance.size()); index++) {
            if (distance[index] >= distance[index - 2] &&
                distance[index - 1] <= distance[index - 3]) {
                return true;
            }
            if (index >= 4 && distance[index - 1] == distance[index - 3]) {
                if (distance[index - 2] >= distance[index - 4] + distance[index]) {
                    return true;
                }
            }
            if (index >= 5) {
                if (distance[index - 4] >= distance[index - 2] - distance[index]) {
                    if (distance[index] >= distance[index - 2] - distance[index - 4]) {
                        if (distance[index - 1] <= distance[index - 3]) {
                            if (distance[index - 5] + distance[index - 1] >= distance[index - 3]) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
        return false;
    }
};
