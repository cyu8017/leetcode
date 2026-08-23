// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

#include <functional>
#include <vector>

class Solution {
public:
    long long countPaths(int n, std::vector<std::vector<int>>& edges) {
        std::vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) isPrime[j] = false;
            }
        }
        std::vector<std::vector<int>> g(n + 1);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::function<int(int, int)> dfs = [&](int u, int p) {
            if (isPrime[u]) return 0;
            int sz = 1;
            for (int v : g[u]) if (v != p) sz += dfs(v, u);
            return sz;
        };
        long long ans = 0;
        for (int u = 1; u <= n; u++) {
            if (!isPrime[u]) continue;
            long long total = 0;
            for (int v : g[u]) {
                int c = dfs(v, u);
                ans += c;
                ans += total * c;
                total += c;
            }
        }
        return ans;
    }
};
