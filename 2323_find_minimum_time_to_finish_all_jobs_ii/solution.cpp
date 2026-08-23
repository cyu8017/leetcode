// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumTime(std::vector<int>& jobs, std::vector<int>& workers) {
        std::sort(jobs.begin(), jobs.end());
        std::sort(workers.begin(), workers.end());
        int ans = 0;
        for (size_t i = 0; i < jobs.size(); ++i)
            ans = std::max(ans, (jobs[i] + workers[i] - 1) / workers[i]);
        return ans;
    }
};
