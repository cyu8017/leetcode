#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int findLucky(std::vector<int>& arr) {
        std::unordered_map<int, int> c;
        for (int x : arr) ++c[x];
        int ans = -1;
        for (auto [x, cnt] : c) if (x == cnt) ans = std::max(ans, x);
        return ans;
    }
};
