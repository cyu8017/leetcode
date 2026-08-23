// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> findRelativeRanks(std::vector<int>& score) {
        static const std::unordered_map<int, std::string> medals = {
            {1, "Gold Medal"},
            {2, "Silver Medal"},
            {3, "Bronze Medal"},
        };
        std::vector<int> order(score.size());
        for (size_t index = 0; index < order.size(); ++index) {
            order[index] = static_cast<int>(index);
        }
        std::sort(order.begin(), order.end(),
                  [&](int left, int right) { return score[left] > score[right]; });

        std::vector<std::string> result(score.size());
        for (size_t rank = 0; rank < order.size(); ++rank) {
            const int medalRank = static_cast<int>(rank) + 1;
            auto it = medals.find(medalRank);
            if (it != medals.end()) {
                result[order[rank]] = it->second;
            } else {
                result[order[rank]] = std::to_string(medalRank);
            }
        }
        return result;
    }
};
