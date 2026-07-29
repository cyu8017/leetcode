// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

#include <numeric>
#include <vector>

class Solution {
public:
    int dietPlanPerformance(std::vector<int>& calories, int k, int lower, int upper) {
        int window = std::accumulate(calories.begin(), calories.begin() + k, 0);
        int ans = 0;
        if (window < lower) --ans;
        else if (window > upper) ++ans;
        for (int i = k; i < static_cast<int>(calories.size()); ++i) {
            window += calories[i] - calories[i - k];
            if (window < lower) --ans;
            else if (window > upper) ++ans;
        }
        return ans;
    }
};
