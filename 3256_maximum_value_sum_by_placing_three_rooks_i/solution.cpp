// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

#include <cstdint>
#include <vector>

class Solution {
    struct Cell { int v, c; };

public:
    long long maximumValueSum(std::vector<std::vector<int>>& board) {
        int m = (int)board.size(), n = (int)board[0].size();
        std::vector<std::vector<Cell>> tops(m);
        for (int i = 0; i < m; i++) {
            std::vector<Cell> row;
            for (int j = 0; j < n; j++) {
                Cell cur{board[i][j], j};
                bool placed = false;
                for (int t = 0; t < (int)row.size(); t++) {
                    if (cur.v > row[t].v) {
                        row.insert(row.begin() + t, cur);
                        placed = true;
                        break;
                    }
                }
                if (!placed) row.push_back(cur);
                if ((int)row.size() > 3) row.resize(3);
            }
            tops[i] = row;
        }
        int64_t ans = -(1LL << 62);
        for (int i = 0; i < m; i++) {
            for (auto& a : tops[i]) {
                for (int j = i + 1; j < m; j++) {
                    for (auto& b : tops[j]) {
                        if (a.c == b.c) continue;
                        for (int k = j + 1; k < m; k++) {
                            for (auto& c : tops[k]) {
                                if (c.c == a.c || c.c == b.c) continue;
                                int64_t s = (int64_t)a.v + b.v + c.v;
                                if (s > ans) ans = s;
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};
