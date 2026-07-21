// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minSkips(std::vector<int>& dist, int speed, int hoursBefore) {
        long long limit = 1LL * hoursBefore * speed;
        int n = static_cast<int>(dist.size());
        const long long INF = LLONG_MAX / 4;
        std::vector<long long> dp(n + 1, INF);
        dp[0] = 0;

        for (int road : dist) {
            std::vector<long long> nxt(n + 1, INF);
            for (int skips = 0; skips < n; skips++) {
                if (dp[skips] == INF) continue;
                nxt[skips] = std::min(nxt[skips], ((dp[skips] + road + speed - 1) / speed) * speed);
                nxt[skips + 1] = std::min(nxt[skips + 1], dp[skips] + road);
            }
            dp.swap(nxt);
        }

        for (int skips = 0; skips <= n; skips++) {
            if (dp[skips] <= limit) {
                return skips;
            }
        }
        return -1;
    }
};
