// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

#include <unordered_map>
#include <vector>

class Solution {
    static constexpr int mx = 1000001;
    static std::vector<std::vector<int>>& factors() {
        static std::vector<std::vector<int>> f;
        if (f.empty()) {
            f.assign(mx, {});
            for (int i = 2; i < mx; i++) {
                if (f[i].empty()) {
                    for (int j = i; j < mx; j += i) f[j].push_back(i);
                }
            }
        }
        return f;
    }

public:
    int minJumps(std::vector<int>& nums) {
        auto& fac = factors();
        int n = (int)nums.size();
        std::unordered_map<int, std::vector<int>> g;
        for (int i = 0; i < n; i++)
            for (int p : fac[nums[i]]) g[p].push_back(i);
        int ans = 0;
        std::vector<bool> vis(n);
        vis[0] = true;
        std::vector<int> q{0};
        while (true) {
            std::vector<int> nq;
            for (int i : q) {
                if (i == n - 1) return ans;
                std::vector<int> idx = g[nums[i]];
                idx.push_back(i + 1);
                if (i > 0) idx.push_back(i - 1);
                for (int j : idx) {
                    if (j >= 0 && j < n && !vis[j]) {
                        vis[j] = true;
                        nq.push_back(j);
                    }
                }
                g[nums[i]].clear();
            }
            q = std::move(nq);
            ans++;
        }
    }
};
