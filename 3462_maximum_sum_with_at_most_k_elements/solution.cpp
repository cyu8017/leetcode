// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    long long maxSum(std::vector<std::vector<int>>& grid, std::vector<int>& limits, int k) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> h;
        long long sum = 0;
        for (int i = 0; i < (int)grid.size(); i++) {
            std::vector<int> r = grid[i];
            std::sort(r.rbegin(), r.rend());
            int lim = limits[i];
            if (lim > (int)r.size()) lim = (int)r.size();
            for (int j = 0; j < lim; j++) {
                h.push(r[j]);
                sum += r[j];
                if ((int)h.size() > k) {
                    sum -= h.top();
                    h.pop();
                }
            }
        }
        return sum;
    }
};
