// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long minCost(std::vector<int>& basket1, std::vector<int>& basket2) {
        std::unordered_map<int, int> freq;
        int mn = 1 << 30;
        for (int x : basket1) {
            freq[x]++;
            mn = std::min(mn, x);
        }
        for (int x : basket2) {
            freq[x]--;
            mn = std::min(mn, x);
        }
        std::vector<int> extra;
        for (auto& [v, c] : freq) {
            if (c % 2 != 0) return -1;
            for (int i = 0; i < std::abs(c) / 2; ++i) extra.push_back(v);
        }
        std::sort(extra.begin(), extra.end());
        long long ans = 0;
        for (int i = 0; i < (int)extra.size() / 2; ++i) {
            long long a = extra[i];
            long long b = 2LL * mn;
            ans += std::min(a, b);
        }
        return ans;
    }
};
