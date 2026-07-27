// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxScoreSightseeingPair(std::vector<int>& values) {
        int best = values[0];
        int ans = 0;
        for (int j = 1; j < static_cast<int>(values.size()); ++j) {
            ans = std::max(ans, best + values[j] - j);
            best = std::max(best, values[j] + j);
        }
        return ans;
    }
};

