// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string shortestSuperstring(std::vector<std::string>& words) {
        int n = (int)words.size();
        std::vector<std::vector<int>> overlap(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                const auto& a = words[i];
                const auto& b = words[j];
                for (int k = (int)std::min(a.size(), b.size()); k > 0; k--) {
                    if (a.compare(a.size() - k, k, b, 0, k) == 0) {
                        overlap[i][j] = k;
                        break;
                    }
                }
            }
        }
        int N = 1 << n;
        std::vector<std::vector<std::string>> dp(N, std::vector<std::string>(n));
        for (int i = 0; i < n; i++) dp[1 << i][i] = words[i];
        for (int mask = 0; mask < N; mask++) {
            for (int last = 0; last < n; last++) {
                if (!(mask & (1 << last)) || dp[mask][last].empty()) continue;
                for (int nxt = 0; nxt < n; nxt++) {
                    if (mask & (1 << nxt)) continue;
                    std::string cand = dp[mask][last] + words[nxt].substr(overlap[last][nxt]);
                    int nmask = mask | (1 << nxt);
                    if (dp[nmask][nxt].empty() || cand.size() < dp[nmask][nxt].size())
                        dp[nmask][nxt] = cand;
                }
            }
        }
        int full = N - 1;
        std::string best;
        for (int i = 0; i < n; i++) {
            if (!dp[full][i].empty() && (best.empty() || dp[full][i].size() < best.size()))
                best = dp[full][i];
        }
        return best;
    }
};
