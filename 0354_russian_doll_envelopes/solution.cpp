// LeetCode 0354 - Russian Doll Envelopes
// https://leetcode.com/problems/russian-doll-envelopes/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxEnvelopes(std::vector<std::vector<int>>& envelopes) {
        std::sort(envelopes.begin(), envelopes.end(), [](const std::vector<int>& left, const std::vector<int>& right) {
            if (left[0] != right[0]) {
                return left[0] < right[0];
            }
            return left[1] > right[1];
        });

        std::vector<int> tails;
        for (const auto& envelope : envelopes) {
            int height = envelope[1];
            auto position = std::lower_bound(tails.begin(), tails.end(), height);
            if (position == tails.end()) {
                tails.push_back(height);
            } else {
                *position = height;
            }
        }

        return static_cast<int>(tails.size());
    }
};
