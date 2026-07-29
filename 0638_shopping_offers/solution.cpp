// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

#include <algorithm>
#include <map>
#include <vector>

class Solution {
    std::vector<int> price_;
    std::vector<std::vector<int>> special_;
    std::map<std::vector<int>, int> memo_;

    int dfs(std::vector<int> state) {
        if (memo_.count(state)) {
            return memo_[state];
        }
        int cost = 0;
        for (std::size_t i = 0; i < price_.size(); ++i) {
            cost += state[i] * price_[i];
        }
        for (const auto& offer : special_) {
            std::vector<int> nxt = state;
            bool valid = true;
            for (std::size_t i = 0; i < price_.size(); ++i) {
                if (nxt[i] < offer[i]) {
                    valid = false;
                    break;
                }
                nxt[i] -= offer[i];
            }
            if (valid) {
                cost = std::min(cost, offer[price_.size()] + dfs(nxt));
            }
        }
        return memo_[state] = cost;
    }

public:
    int shoppingOffers(std::vector<int>& price, std::vector<std::vector<int>>& special,
                       std::vector<int>& needs) {
        price_ = price;
        special_ = special;
        memo_.clear();
        return dfs(needs);
    }
};
