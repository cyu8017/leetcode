// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

#include <algorithm>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int maxCapacity(std::vector<int>& costs, std::vector<int>& capacity, int budget) {
        std::vector<std::pair<int, int>> arr;
        for (int k = 0; k < (int)costs.size(); k++) {
            if (costs[k] < budget) arr.push_back({costs[k], capacity[k]});
        }
        if (arr.empty()) return 0;
        std::sort(arr.begin(), arr.end());
        int m = (int)arr.size();
        std::vector<char> alive(m, 1);
        using Node = std::pair<int, int>;
        auto cmp = [](const Node& a, const Node& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        };
        std::priority_queue<Node, std::vector<Node>, decltype(cmp)> h(cmp);
        for (int i = 0; i < m; i++) h.push({arr[i].second, i});
        while (!h.empty() && !alive[h.top().second]) h.pop();
        int ans = h.top().first;
        int i = 0, j = m - 1;
        while (i < j) {
            alive[i] = 0;
            while (i < j && arr[i].first + arr[j].first >= budget) {
                alive[j] = 0;
                j--;
            }
            while (!h.empty() && !alive[h.top().second]) h.pop();
            if (!h.empty()) ans = std::max(ans, arr[i].second + h.top().first);
            i++;
        }
        return ans;
    }
};
