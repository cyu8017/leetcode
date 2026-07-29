#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    std::vector<int> kWeakestRows(std::vector<std::vector<int>>& mat, int k) {
        std::vector<int> idx(mat.size());
        std::iota(idx.begin(), idx.end(), 0);
        std::sort(idx.begin(), idx.end(), [&](int a, int b) {
            int sa = std::accumulate(mat[a].begin(), mat[a].end(), 0);
            int sb = std::accumulate(mat[b].begin(), mat[b].end(), 0);
            return sa != sb ? sa < sb : a < b;
        });
        idx.resize(k);
        return idx;
    }
};
