#include <vector>

class Solution {
public:
    std::vector<int> finalPrices(std::vector<int>& prices) {
        std::vector<int> ans = prices;
        std::vector<int> stack;
        for (int i = 0; i < (int)prices.size(); ++i) {
            while (!stack.empty() && prices[stack.back()] >= prices[i]) {
                int j = stack.back(); stack.pop_back();
                ans[j] -= prices[i];
            }
            stack.push_back(i);
        }
        return ans;
    }
};
