// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

#include <vector>
#include <algorithm>

class Solution {
    struct FenwickMax {
        std::vector<int> vals;
        FenwickMax(int n) : vals(n + 1) {}
        void maximize(int i, int val) {
            for (; i < (int)vals.size(); i += i & -i)
                vals[i] = std::max(vals[i], val);
        }
        int get(int i) {
            int res = 0;
            for (; i > 0; i -= i & -i) res = std::max(res, vals[i]);
            return res;
        }
    };
public:
    std::vector<bool> getResults(std::vector<std::vector<int>>& queries) {
        int n = (int)queries.size() * 3;
        if (n > 50000) n = 50000;
        FenwickMax tree(n + 1);
        std::vector<int> obs = {0, n};
        for (auto& q : queries) {
            if (q[0] == 1) {
                int x = q[1];
                auto it = std::lower_bound(obs.begin(), obs.end(), x);
                if (it == obs.end() || *it != x) obs.insert(it, x);
            }
        }
        for (int i = 0; i + 1 < (int)obs.size(); i++) {
            tree.maximize(obs[i + 1], obs[i + 1] - obs[i]);
        }
        std::vector<bool> ans;
        for (int i = (int)queries.size() - 1; i >= 0; i--) {
            int typ = queries[i][0], x = queries[i][1];
            if (typ == 1) {
                auto it = std::lower_bound(obs.begin(), obs.end(), x);
                int j = (int)(it - obs.begin());
                int prev = obs[j - 1], next = obs[j + 1];
                obs.erase(it);
                tree.maximize(next, next - prev);
            } else {
                int sz = queries[i][2];
                int j = (int)(std::lower_bound(obs.begin(), obs.end(), x + 1) - obs.begin()) - 1;
                int prev = obs[j];
                ans.push_back(tree.get(prev) >= sz || x - prev >= sz);
            }
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};
