// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& prices) {
        std::unordered_map<int, long long> best;
        long long ans = 0;
        for (int i = 0; i < (int)prices.size(); i++) {
            int key = prices[i] - (i + 1);
            long long cand = best[key] + prices[i];
            if (cand > best[key]) best[key] = cand;
            if (best[key] > ans) ans = best[key];
        }
        return ans;
    }
};
