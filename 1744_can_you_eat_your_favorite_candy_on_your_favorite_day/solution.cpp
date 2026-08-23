// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

#include <vector>

class Solution {
public:
    std::vector<bool> canEat(std::vector<int>& candiesCount, std::vector<std::vector<int>>& queries) {
        std::vector<long long> prefix(candiesCount.size() + 1, 0);
        for (size_t i = 0; i < candiesCount.size(); i++) {
            prefix[i + 1] = prefix[i] + candiesCount[i];
        }
        std::vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& query : queries) {
            int candyType = query[0];
            long long day = query[1];
            long long cap = query[2];
            long long minEaten = day + 1;
            long long maxEaten = (day + 1) * cap;
            ans.push_back(maxEaten > prefix[candyType] && minEaten <= prefix[candyType + 1]);
        }
        return ans;
    }
};
