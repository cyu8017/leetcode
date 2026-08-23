// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxProfit(std::vector<int>& workers, std::vector<std::vector<int>>& tasks) {
        std::sort(workers.begin(), workers.end());
        std::sort(tasks.begin(), tasks.end(), [](auto& a, auto& b) { return a[0] < b[0]; });
        long long ans = 0;
        std::vector<bool> used(tasks.size(), false);
        for (int w : workers) {
            int best = -1, bi = -1;
            for (int i = 0; i < (int)tasks.size(); i++) {
                if (used[i]) continue;
                if (tasks[i][0] > w) break;
                if (tasks[i][1] > best) {
                    best = tasks[i][1];
                    bi = i;
                }
            }
            if (bi >= 0) {
                used[bi] = true;
                ans += best;
            }
        }
        return ans;
    }
};
