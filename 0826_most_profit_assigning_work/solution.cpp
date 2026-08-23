// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

#include <algorithm>
#include <utility>
#include <vector>

class Solution {
public:
    int maxProfitAssignment(std::vector<int>& difficulty, std::vector<int>& profit,
                            std::vector<int>& worker) {
        std::vector<std::pair<int, int>> jobs;
        for (size_t i = 0; i < difficulty.size(); ++i) {
            jobs.emplace_back(difficulty[i], profit[i]);
        }
        std::sort(jobs.begin(), jobs.end());
        std::sort(worker.begin(), worker.end());
        int ans = 0, best = 0, i = 0;
        for (int ability : worker) {
            while (i < static_cast<int>(jobs.size()) && jobs[i].first <= ability) {
                best = std::max(best, jobs[i].second);
                ++i;
            }
            ans += best;
        }
        return ans;
    }
};
