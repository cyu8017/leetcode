#include <deque>
#include <climits>
#include <utility>
#include <vector>

class Solution {
public:
    int findMaxValueOfEquation(std::vector<std::vector<int>>& points, int k) {
        std::deque<std::pair<int,int>> q;
        long long ans = LLONG_MIN / 4;
        for (auto& p : points) {
            int x = p[0], y = p[1];
            while (!q.empty() && x - q.front().first > k) q.pop_front();
            if (!q.empty()) ans = std::max(ans, (long long)x + y + q.front().second);
            int value = y - x;
            while (!q.empty() && q.back().second <= value) q.pop_back();
            q.push_back({x, value});
        }
        return (int)ans;
    }
};
