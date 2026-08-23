// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

#include <cstdint>
#include <unordered_map>
#include <vector>

class Solution {
    struct UnionFind {
        std::unordered_map<int64_t, int64_t> p;
        std::unordered_map<int64_t, int> size;
        int64_t find(int64_t x) {
            if (!p.count(x)) {
                p[x] = x;
                size[x] = 1;
            }
            if (p[x] != x) p[x] = find(p[x]);
            return p[x];
        }
        bool unite(int64_t a, int64_t b) {
            int64_t pa = find(a), pb = find(b);
            if (pa == pb) return false;
            if (size[pa] > size[pb]) {
                p[pb] = pa;
                size[pa] += size[pb];
            } else {
                p[pa] = pb;
                size[pb] += size[pa];
            }
            return true;
        }
    };

public:
    int maxActivated(std::vector<std::vector<int>>& points) {
        UnionFind uf;
        const int64_t m = 3000000000LL;
        for (auto& pt : points) uf.unite(pt[0], pt[1] + m);
        std::unordered_map<int64_t, int> cnt;
        for (auto& pt : points) cnt[uf.find(pt[0])]++;
        int mx1 = 0, mx2 = 0;
        for (auto& [_, x] : cnt) {
            if (mx1 < x) {
                mx2 = mx1;
                mx1 = x;
            } else if (mx2 < x) {
                mx2 = x;
            }
        }
        return mx1 + mx2 + 1;
    }
};
