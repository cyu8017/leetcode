// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int closestCost(std::vector<int>& baseCosts, std::vector<int>& toppingCosts, int target) {
        best_ = 1 << 29;
        target_ = target;
        toppings_ = &toppingCosts;
        for (int base : baseCosts) {
            dfs(0, base);
        }
        return best_;
    }

private:
    int best_;
    int target_;
    std::vector<int>* toppings_;

    void dfs(int i, int cur) {
        int curDiff = std::abs(cur - target_);
        int bestDiff = std::abs(best_ - target_);
        if (curDiff < bestDiff || (curDiff == bestDiff && cur < best_)) {
            best_ = cur;
        }
        if (i == (int)toppings_->size() || cur >= target_) {
            return;
        }
        dfs(i + 1, cur);
        dfs(i + 1, cur + (*toppings_)[i]);
        dfs(i + 1, cur + 2 * (*toppings_)[i]);
    }
};
