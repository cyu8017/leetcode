// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> minReverseOperations(int n, int p, std::vector<int>& banned, int k) {
        std::unordered_set<int> ban(banned.begin(), banned.end());
        std::vector<int> ans(n, -1);
        ans[p] = 0;
        std::queue<std::pair<int, int>> q;
        q.push({p, 0});
        while (!q.empty()) {
            auto [i, d] = q.front();
            q.pop();
            int lo = i - (k - 1);
            if (lo < 0) lo = 0;
            int hi = i;
            if (hi > n - k) hi = n - k;
            for (int L = lo; L <= hi; ++L) {
                int R = L + k - 1;
                int ni = L + R - i;
                if (ni < 0 || ni >= n || ban.count(ni) || ans[ni] != -1) continue;
                ans[ni] = d + 1;
                q.push({ni, d + 1});
            }
        }
        return ans;
    }
};
