// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int xorAfterQueries(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        const int MOD = 1000000007;
        int n = (int)nums.size();
        struct Upd { int l, r, k, v; };
        std::unordered_map<int, std::vector<Upd>> byK;
        for (auto& q : queries) byK[q[2]].push_back({q[0], q[1], q[2], q[3]});
        std::vector<int> res = nums;
        for (auto& [k, ups] : byK) {
            std::vector<int> fac(n, 1);
            for (auto& u : ups)
                for (int i = u.l; i <= u.r; i += k) fac[i] = 1LL * fac[i] * u.v % MOD;
            for (int i = 0; i < n; i++) res[i] = 1LL * res[i] * fac[i] % MOD;
        }
        int ans = 0;
        for (int v : res) ans ^= v;
        return ans;
    }
};
