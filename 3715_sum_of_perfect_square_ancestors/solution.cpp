// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

#include <functional>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long sumOfAncestors(int n, std::vector<std::vector<int>>& edges, std::vector<int>& nums) {
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        auto kernel = [](int x) {
            int res = 1;
            for (int p = 2; p * p <= x; p++) {
                int cnt = 0;
                while (x % p == 0) { x /= p; cnt++; }
                if (cnt % 2 == 1) res *= p;
            }
            if (x > 1) res *= x;
            return res;
        };
        std::vector<int> ks(n);
        for (int i = 0; i < n; i++) ks[i] = kernel(nums[i]);
        std::unordered_map<int, int> freq;
        long long ans = 0;
        std::function<void(int, int)> dfs = [&](int u, int p) {
            ans += freq[ks[u]];
            freq[ks[u]]++;
            for (int v : graph[u]) if (v != p) dfs(v, u);
            freq[ks[u]]--;
        };
        dfs(0, -1);
        return ans;
    }
};
