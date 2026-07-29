#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    int maxPerformance(int n, std::vector<int>& speed, std::vector<int>& efficiency, int k) {
        std::vector<std::pair<int, int>> eng;
        for (int i = 0; i < n; ++i) eng.push_back({efficiency[i], speed[i]});
        std::sort(eng.rbegin(), eng.rend());
        std::priority_queue<int, std::vector<int>, std::greater<int>> h;
        long long total = 0, ans = 0;
        for (auto [e, s] : eng) {
            h.push(s); total += s;
            if ((int)h.size() > k) { total -= h.top(); h.pop(); }
            ans = std::max(ans, total * e);
        }
        return (int)(ans % 1000000007);
    }
};
