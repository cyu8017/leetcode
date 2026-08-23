// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maxTotal(std::vector<int>& value, std::vector<int>& limit) {
        std::unordered_map<int, std::vector<int>> g;
        for (int i = 0; i < (int)value.size(); i++) g[limit[i]].push_back(value[i]);
        long long ans = 0;
        for (auto& [lim, vs] : g) {
            std::sort(vs.begin(), vs.end(), std::greater<int>());
            for (int i = 0; i < std::min(lim, (int)vs.size()); i++) ans += vs[i];
        }
        return ans;
    }
};
