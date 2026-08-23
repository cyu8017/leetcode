// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

#include <vector>
#include <algorithm>

class Solution {
public:
    int countDays(int days, std::vector<std::vector<int>>& meetings) {
        std::sort(meetings.begin(), meetings.end());
        int last = 0, ans = 0;
        for (auto& e : meetings) {
            int st = e[0], ed = e[1];
            if (last < st) ans += st - last - 1;
            last = std::max(last, ed);
        }
        ans += days - last;
        return ans;
    }
};
