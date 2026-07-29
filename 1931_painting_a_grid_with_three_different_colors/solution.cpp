// LeetCode 1931 - Painting a Grid With Three Different Colors
#include <functional>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int colorTheGrid(int m, int n) {
        const int MOD = 1000000007;
        auto valid = [&](int mask) {
            int prev = -1;
            for (int i = 0; i < m; i++) {
                int c = mask % 3;
                if (c == prev) return false;
                prev = c;
                mask /= 3;
            }
            return true;
        };
        auto colors = [&](int mask) {
            std::vector<int> cols;
            for (int i = 0; i < m; i++) {
                cols.push_back(mask % 3);
                mask /= 3;
            }
            return cols;
        };
        int lim = 1;
        for (int i = 0; i < m; i++) lim *= 3;
        std::vector<int> states;
        for (int s = 0; s < lim; s++) if (valid(s)) states.push_back(s);
        std::unordered_map<int, std::vector<int>> compat;
        for (int a : states) {
            auto ca = colors(a);
            for (int b : states) {
                auto cb = colors(b);
                bool ok = true;
                for (int i = 0; i < m; i++) if (ca[i] == cb[i]) { ok = false; break; }
                if (ok) compat[a].push_back(b);
            }
        }
        std::unordered_map<long long, int> memo;
        std::function<int(int, int)> dp = [&](int col, int prev) -> int {
            if (col == n) return 1;
            long long key = ((long long)col << 20) | (prev + 1);
            if (memo.count(key)) return memo[key];
            long long total = 0;
            const std::vector<int>& opts = (prev == -1) ? states : compat[prev];
            for (int cur : opts) total = (total + dp(col + 1, cur)) % MOD;
            return memo[key] = (int)total;
        };
        return dp(0, -1);
    }
};
