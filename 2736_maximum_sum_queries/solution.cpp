// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

#include <vector>
#include <algorithm>
#include <map>

class Solution {
public:
    std::vector<int> maximumSumQueries(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<std::vector<int>>& queries) {
        int n = (int)nums1.size();
        struct Pair { int x, y, s; };
        std::vector<Pair> pts(n);
        for (int i = 0; i < n; i++) pts[i] = {nums1[i], nums2[i], nums1[i] + nums2[i]};
        std::sort(pts.begin(), pts.end(), [](auto& a, auto& b) { return a.x > b.x; });
        struct Qi { int x, y, i; };
        std::vector<Qi> qs(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) qs[i] = {queries[i][0], queries[i][1], i};
        std::sort(qs.begin(), qs.end(), [](auto& a, auto& b) { return a.x > b.x; });
        std::vector<int> ys = nums2;
        for (auto& q : queries) ys.push_back(q[1]);
        std::sort(ys.begin(), ys.end());
        ys.erase(std::unique(ys.begin(), ys.end()), ys.end());
        auto rank = [&](int y) {
            return (int)(std::lower_bound(ys.begin(), ys.end(), y) - ys.begin()) + 1;
        };
        int m = (int)ys.size();
        std::vector<int> bit(m + 2, -1);
        auto update = [&](int i, int v) {
            for (; i <= m; i += i & -i) bit[i] = std::max(bit[i], v);
        };
        auto query = [&](int i) {
            int best = -1;
            for (; i > 0; i -= i & -i) best = std::max(best, bit[i]);
            return best;
        };
        std::vector<int> ans(queries.size());
        int j = 0;
        for (auto& q : qs) {
            while (j < n && pts[j].x >= q.x) {
                update(m - rank(pts[j].y) + 1, pts[j].s);
                j++;
            }
            ans[q.i] = query(m - rank(q.y) + 1);
        }
        return ans;
    }
};
