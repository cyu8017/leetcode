#include <algorithm>
#include <deque>
#include <vector>

class Solution {
public:
    int constrainedSubsetSum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> best = nums;
        std::deque<int> queue;
        for (int i = 0; i < n; ++i) {
            while (!queue.empty() && queue.front() < i - k) queue.pop_front();
            best[i] = nums[i] + std::max(0, queue.empty() ? 0 : best[queue.front()]);
            while (!queue.empty() && best[queue.back()] <= best[i]) queue.pop_back();
            queue.push_back(i);
        }
        return *std::max_element(best.begin(), best.end());
    }
};
