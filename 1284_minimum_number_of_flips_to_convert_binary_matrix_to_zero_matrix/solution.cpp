// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minFlips(std::vector<std::vector<int>>& mat) {
        const int m = static_cast<int>(mat.size());
        const int n = static_cast<int>(mat[0].size());
        int start = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                start |= mat[r][c] << (r * n + c);
            }
        }
        std::vector<int> masks;
        static const int dr[] = {0, 1, -1, 0, 0};
        static const int dc[] = {0, 0, 0, 1, -1};
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                int mask = 0;
                for (int i = 0; i < 5; ++i) {
                    int nr = r + dr[i], nc = c + dc[i];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        mask ^= 1 << (nr * n + nc);
                    }
                }
                masks.push_back(mask);
            }
        }
        std::queue<std::pair<int, int>> q;
        std::unordered_set<int> seen{start};
        q.push({start, 0});
        while (!q.empty()) {
            auto [state, distance] = q.front();
            q.pop();
            if (state == 0) {
                return distance;
            }
            for (int mask : masks) {
                int nxt = state ^ mask;
                if (!seen.count(nxt)) {
                    seen.insert(nxt);
                    q.push({nxt, distance + 1});
                }
            }
        }
        return -1;
    }
};
