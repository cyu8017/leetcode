#include <algorithm>
#include <set>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> avoidFlood(std::vector<int>& rains) {
        int n = (int)rains.size();
        std::vector<int> ans(n, -1);
        std::unordered_map<int, int> full;
        std::set<int> dry;
        for (int i = 0; i < n; ++i) {
            int lake = rains[i];
            if (lake == 0) {
                dry.insert(i);
                ans[i] = 1;
            } else {
                if (full.count(lake)) {
                    auto it = dry.upper_bound(full[lake]);
                    if (it == dry.end()) return {};
                    ans[*it] = lake;
                    dry.erase(it);
                }
                full[lake] = i;
            }
        }
        return ans;
    }
};
