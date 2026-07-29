#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minDifficulty(std::vector<int>& jobDifficulty, int d) {
        int n = (int)jobDifficulty.size();
        if (n < d) return -1;
        const int INF = 1e9;
        std::vector<int> dp(n, INF);
        int hardest = 0;
        for (int i = 0; i < n; ++i) {
            hardest = std::max(hardest, jobDifficulty[i]);
            dp[i] = hardest;
        }
        for (int day = 1; day < d; ++day) {
            std::vector<int> nxt(n, INF);
            for (int end = day; end < n; ++end) {
                hardest = 0;
                for (int start = end; start >= day; --start) {
                    hardest = std::max(hardest, jobDifficulty[start]);
                    nxt[end] = std::min(nxt[end], dp[start - 1] + hardest);
                }
            }
            dp = std::move(nxt);
        }
        return dp.back();
    }
};
