// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generateSchedule(int n) {
        if (n < 5) return {};
        std::vector<std::vector<int>> matches;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) matches.push_back({i, j});
            }
        }
        std::vector<bool> used(matches.size(), false);
        std::vector<std::vector<int>> sched;
        int last0 = -1, last1 = -1;
        std::function<bool()> dfs = [&]() -> bool {
            if ((int)sched.size() == (int)matches.size()) return true;
            for (int i = 0; i < (int)matches.size(); i++) {
                if (used[i]) continue;
                auto& m = matches[i];
                if (m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1) continue;
                used[i] = true;
                sched.push_back(m);
                int p0 = last0, p1 = last1;
                last0 = m[0]; last1 = m[1];
                if (dfs()) return true;
                last0 = p0; last1 = p1;
                sched.pop_back();
                used[i] = false;
            }
            return false;
        };
        if (dfs()) return sched;
        return {};
    }
};
