// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int distributeCandies(std::vector<int>& candyType) {
        std::unordered_set<int> unique(candyType.begin(), candyType.end());
        return static_cast<int>(
            std::min(unique.size(), candyType.size() / 2));
    }
};
