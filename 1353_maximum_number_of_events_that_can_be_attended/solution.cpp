#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    int maxEvents(std::vector<std::vector<int>>& events) {
        std::sort(events.begin(), events.end());
        std::priority_queue<int, std::vector<int>, std::greater<int>> h;
        int i = 0, ans = 0, day = 0, n = (int)events.size();
        while (i < n || !h.empty()) {
            if (h.empty()) day = std::max(day, events[i][0]);
            while (i < n && events[i][0] <= day) h.push(events[i++][1]);
            while (!h.empty() && h.top() < day) h.pop();
            if (!h.empty()) {
                h.pop();
                ++ans;
                ++day;
            }
        }
        return ans;
    }
};
