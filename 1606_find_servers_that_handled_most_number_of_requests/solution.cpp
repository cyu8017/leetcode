// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

#include <algorithm>
#include <queue>
#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> busiestServers(int k, std::vector<int>& arrival, std::vector<int>& load) {
        std::set<int> free;
        for (int i = 0; i < k; ++i) {
            free.insert(i);
        }
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> busy;
        std::vector<int> count(k, 0);
        for (int i = 0; i < static_cast<int>(arrival.size()); ++i) {
            const int t = arrival[i];
            while (!busy.empty() && busy.top().first <= t) {
                free.insert(busy.top().second);
                busy.pop();
            }
            if (free.empty()) {
                continue;
            }
            auto it = free.lower_bound(i % k);
            if (it == free.end()) {
                it = free.begin();
            }
            const int server = *it;
            free.erase(it);
            ++count[server];
            busy.push({t + load[i], server});
        }
        const int best = *std::max_element(count.begin(), count.end());
        std::vector<int> ans;
        for (int i = 0; i < k; ++i) {
            if (count[i] == best) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
