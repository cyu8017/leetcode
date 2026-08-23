// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

#include <vector>

class Solution {
public:
    int countNonAdjacentSubsets(std::vector<int>& parent, std::vector<int>& nums, int k) {
        const long long mod = 1000000007;
        int n = (int)parent.size();
        std::vector<std::vector<int>> children(n);
        for (int i = 1; i < n; i++) children[parent[i]].push_back(i);
        std::vector<std::vector<long long>> dp0(n), dp1(n);
        for (int u = n - 1; u >= 0; u--) {
            std::vector<long long> a(k, 0), b(k, 0);
            a[0] = 1;
            b[((nums[u] % k) + k) % k] = 1;
            for (int v : children[u]) {
                std::vector<long long> na(k, 0), nb(k, 0);
                for (int x = 0; x < k; x++) {
                    for (int y = 0; y < k; y++) {
                        long long allChild = (dp0[v][y] + dp1[v][y]) % mod;
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % mod;
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod;
                    }
                }
                a.swap(na);
                b.swap(nb);
            }
            dp0[u] = a;
            dp1[u] = b;
        }
        long long ans = (dp0[0][0] + dp1[0][0] - 1) % mod;
        if (ans < 0) ans += mod;
        return (int)ans;
    }
};
