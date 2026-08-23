// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

#include <algorithm>
#include <vector>

class Solution {
public:
    int largestAltitude(std::vector<int>& gain) {
        int altitude = 0;
        int best = 0;
        for (int change : gain) {
            altitude += change;
            best = std::max(best, altitude);
        }
        return best;
    }
};
