// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestWPI(std::vector<int>& hours) {
        int score = 0, ans = 0;
        std::unordered_map<int, int> firstSeen{{0, -1}};
        for (int i = 0; i < static_cast<int>(hours.size()); ++i) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) ans = i + 1;
            else if (firstSeen.count(score - 1)) ans = std::max(ans, i - firstSeen[score - 1]);
            if (!firstSeen.count(score)) firstSeen[score] = i;
        }
        return ans;
    }
};
