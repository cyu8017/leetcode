// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

#include <algorithm>
#include <deque>
#include <vector>

class Solution {
public:
    int maximumRobots(std::vector<int>& chargeTimes, std::vector<int>& runningCosts, long long budget) {
        int n = (int)chargeTimes.size();
        int left = 0;
        long long sum = 0;
        std::deque<int> dq;
        int ans = 0;
        for (int right = 0; right < n; right++) {
            while (!dq.empty() && chargeTimes[dq.back()] <= chargeTimes[right]) dq.pop_back();
            dq.push_back(right);
            sum += runningCosts[right];
            while (left <= right && (long long)chargeTimes[dq.front()] + (long long)(right - left + 1) * sum > budget) {
                if (dq.front() == left) dq.pop_front();
                sum -= runningCosts[left];
                left++;
            }
            ans = std::max(ans, right - left + 1);
        }
        return ans;
    }
};
