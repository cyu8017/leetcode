// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

#include <algorithm>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    double mincostToHireWorkers(std::vector<int>& quality, std::vector<int>& wage,
                                int k) {
        int n = static_cast<int>(quality.size());
        std::vector<std::pair<double, int>> workers;
        for (int i = 0; i < n; ++i) {
            workers.emplace_back(static_cast<double>(wage[i]) / quality[i],
                                 quality[i]);
        }
        std::sort(workers.begin(), workers.end());
        std::priority_queue<int> heap;
        long long totalQ = 0;
        double ans = 1e18;
        for (auto [ratio, q] : workers) {
            heap.push(q);
            totalQ += q;
            if (static_cast<int>(heap.size()) > k) {
                totalQ -= heap.top();
                heap.pop();
            }
            if (static_cast<int>(heap.size()) == k) {
                ans = std::min(ans, totalQ * ratio);
            }
        }
        return ans;
    }
};
