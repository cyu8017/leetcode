// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int largestComponentSize(std::vector<int>& nums) {
        int mx = *std::max_element(nums.begin(), nums.end());
        std::vector<int> parent(mx + 1);
        for (int i = 0; i <= mx; i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            return parent[x] == x ? x : parent[x] = self(self, parent[x]);
        };
        auto unite = [&](int a, int b) { parent[find(find, a)] = find(find, b); };
        auto factors = [](int x) {
            std::vector<int> res;
            for (int d = 2; 1LL * d * d <= x; d++) {
                if (x % d == 0) {
                    res.push_back(d);
                    while (x % d == 0) x /= d;
                }
            }
            if (x > 1) res.push_back(x);
            return res;
        };
        for (int num : nums)
            for (int f : factors(num)) unite(num, f);
        std::unordered_map<int, int> cnt;
        int ans = 0;
        for (int num : nums) ans = std::max(ans, ++cnt[find(find, num)]);
        return ans;
    }
};
