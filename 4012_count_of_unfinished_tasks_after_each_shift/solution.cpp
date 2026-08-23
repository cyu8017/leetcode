// LeetCode 4012 - Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<int> countTasks(std::vector<int>& tasks, std::vector<int>& shifts) {
        int m = (int)tasks.size(), n = (int)shifts.size();
        std::vector<int64_t> s(m + 1, 0);
        for (int i = 0; i < m; i++) s[i + 1] = s[i] + (int64_t)tasks[i];

        std::vector<int> ans(n, 0);
        int i = 0;
        int64_t cur = 0;

        for (int j = 0; j < n; j++) {
            if ((int64_t)shifts[j] < (int64_t)tasks[i] - cur) {
                cur += (int64_t)shifts[j];
                ans[j] = m - i;
            } else {
                int64_t t = (int64_t)shifts[j] - ((int64_t)tasks[i] - cur);
                if (t >= s[m] - s[i + 1]) {
                    i = 0;
                    cur = 0;
                } else {
                    int l = i + 1, r = m;
                    while (l < r) {
                        int mid = (l + r) >> 1;
                        if (t < s[mid + 1] - s[i + 1]) r = mid;
                        else l = mid + 1;
                    }
                    cur = t - (s[l] - s[i + 1]);
                    i = l;
                    ans[j] = m - i;
                }
            }
        }
        return ans;
    }
};
