// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maximumHappinessSum(std::vector<int>& happiness, int k) {
        std::sort(happiness.begin(), happiness.end());
        long long ans = 0;
        for (int i = 0; i < k; i++) {
            int x = happiness[(int)happiness.size() - i - 1] - i;
            ans += std::max(x, 0);
        }
        return ans;
    }
};
