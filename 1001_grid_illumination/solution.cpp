// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> gridIllumination(int n, std::vector<std::vector<int>>& lamps,
                                      std::vector<std::vector<int>>& queries) {
        auto key = [](long long r, long long c) { return (r << 32) ^ c; };
        std::unordered_map<int, int> rows, cols, diag1, diag2;
        std::unordered_set<long long> lit;
        for (auto& lamp : lamps) {
            int r = lamp[0], c = lamp[1];
            long long k = key(r, c);
            if (lit.count(k)) continue;
            lit.insert(k);
            rows[r]++;
            cols[c]++;
            diag1[r - c]++;
            diag2[r + c]++;
        }
        std::vector<int> ans;
        ans.reserve(queries.size());
        for (auto& q : queries) {
            int r = q[0], c = q[1];
            ans.push_back(rows[r] || cols[c] || diag1[r - c] || diag2[r + c] ? 1 : 0);
            for (int i = r - 1; i <= r + 1; ++i) {
                for (int j = c - 1; j <= c + 1; ++j) {
                    long long k = key(i, j);
                    if (!lit.count(k)) continue;
                    lit.erase(k);
                    rows[i]--;
                    cols[j]--;
                    diag1[i - j]--;
                    diag2[i + j]--;
                }
            }
        }
        return ans;
    }
};

