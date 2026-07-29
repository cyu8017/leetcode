// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int orderOfLargestPlusSign(int n, std::vector<std::vector<int>>& mines) {
        std::unordered_set<int> banned;
        for (const auto& mine : mines) {
            banned.insert(mine[0] * n + mine[1]);
        }
        std::vector<std::vector<int>> arms(n, std::vector<int>(n, 0));
        int best = 0;
        for (int r = 0; r < n; ++r) {
            int count = 0;
            for (int c = 0; c < n; ++c) {
                count = banned.count(r * n + c) ? 0 : count + 1;
                arms[r][c] = count;
            }
            count = 0;
            for (int c = n - 1; c >= 0; --c) {
                count = banned.count(r * n + c) ? 0 : count + 1;
                arms[r][c] = std::min(arms[r][c], count);
            }
        }
        for (int c = 0; c < n; ++c) {
            int count = 0;
            for (int r = 0; r < n; ++r) {
                count = banned.count(r * n + c) ? 0 : count + 1;
                arms[r][c] = std::min(arms[r][c], count);
            }
            count = 0;
            for (int r = n - 1; r >= 0; --r) {
                count = banned.count(r * n + c) ? 0 : count + 1;
                arms[r][c] = std::min(arms[r][c], count);
                best = std::max(best, arms[r][c]);
            }
        }
        return best;
    }
};
