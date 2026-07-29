// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

#include <algorithm>
#include <cmath>
#include <functional>
#include <unordered_map>

class Solution {
public:
    int minKnightMoves(int x, int y) {
        x = std::abs(x);
        y = std::abs(y);
        std::unordered_map<long long, int> memo;
        auto key = [](int a, int b) { return (static_cast<long long>(a) << 32) ^ b; };
        std::function<int(int, int)> dfs = [&](int a, int b) -> int {
            if (a + b == 0) return 0;
            if (a + b == 2) return 2;
            long long k = key(a, b);
            if (memo.count(k)) return memo[k];
            return memo[k] = 1 + std::min(dfs(std::abs(a - 1), std::abs(b - 2)),
                                          dfs(std::abs(a - 2), std::abs(b - 1)));
        };
        return dfs(x, y);
    }
};
