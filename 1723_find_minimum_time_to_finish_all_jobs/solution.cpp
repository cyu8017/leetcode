// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

#include <algorithm>
#include <numeric>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimumTimeRequired(std::vector<int>& jobs, int k) {
        std::sort(jobs.begin(), jobs.end(), std::greater<int>());
        std::vector<int> loads(k, 0);
        best = std::accumulate(jobs.begin(), jobs.end(), 0);
        backtrack(0, jobs, loads);
        return best;
    }

private:
    int best;

    void backtrack(int i, const std::vector<int>& jobs, std::vector<int>& loads) {
        if (i == (int)jobs.size()) {
            best = std::min(best, *std::max_element(loads.begin(), loads.end()));
            return;
        }
        std::unordered_set<int> seen;
        for (int worker = 0; worker < (int)loads.size(); worker++) {
            if (seen.count(loads[worker])) {
                continue;
            }
            if (loads[worker] + jobs[i] >= best) {
                continue;
            }
            seen.insert(loads[worker]);
            loads[worker] += jobs[i];
            backtrack(i + 1, jobs, loads);
            loads[worker] -= jobs[i];
            if (loads[worker] == 0) {
                break;
            }
        }
    }
};
