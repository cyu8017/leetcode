// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    long long minimumCost(std::string source, std::string target, std::vector<std::string>& original,
                          std::vector<std::string>& changed, std::vector<int>& cost) {
        const long long inf = 1LL << 60;
        std::unordered_map<std::string, int> ids;
        auto id = [&](const std::string& s) -> int {
            auto it = ids.find(s);
            if (it != ids.end()) return it->second;
            int v = (int)ids.size();
            ids[s] = v;
            return v;
        };
        for (int i = 0; i < (int)original.size(); i++) {
            id(original[i]);
            id(changed[i]);
        }
        int m = (int)ids.size();
        std::vector<std::vector<long long>> dist(m, std::vector<long long>(m, inf));
        for (int i = 0; i < m; i++) dist[i][i] = 0;
        for (int i = 0; i < (int)original.size(); i++) {
            int u = id(original[i]), v = id(changed[i]);
            long long ww = cost[i];
            if (ww < dist[u][v]) dist[u][v] = ww;
        }
        for (int k = 0; k < m; k++)
            for (int i = 0; i < m; i++)
                for (int j = 0; j < m; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
        int n = (int)source.size();
        std::vector<long long> dp(n + 1, inf);
        dp[0] = 0;
        std::unordered_set<int> lens;
        for (auto& kv : ids) lens.insert((int)kv.first.size());
        for (int i = 0; i < n; i++) {
            if (dp[i] >= inf / 2) continue;
            if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
            for (int L : lens) {
                if (i + L > n) continue;
                std::string ss = source.substr(i, L), tt = target.substr(i, L);
                auto iu = ids.find(ss), iv = ids.find(tt);
                if (iu == ids.end() || iv == ids.end()) continue;
                if (dist[iu->second][iv->second] < inf / 2) {
                    long long cand = dp[i] + dist[iu->second][iv->second];
                    if (cand < dp[i + L]) dp[i + L] = cand;
                }
            }
        }
        if (dp[n] >= inf / 2) return -1;
        return dp[n];
    }
};
