// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

#include <vector>
#include <string>

class Solution {
public:
    long long minimumCost(std::string source, std::string target, std::vector<std::string>& original,
                          std::vector<std::string>& changed, std::vector<int>& cost) {
        const long long inf = 1LL << 60;
        std::vector<std::vector<long long>> dist(26, std::vector<long long>(26, inf));
        for (int i = 0; i < 26; i++) dist[i][i] = 0;
        for (int i = 0; i < (int)original.size(); i++) {
            int u = original[i][0] - 'a';
            int v = changed[i][0] - 'a';
            long long ww = cost[i];
            if (ww < dist[u][v]) dist[u][v] = ww;
        }
        for (int k = 0; k < 26; k++)
            for (int i = 0; i < 26; i++)
                for (int j = 0; j < 26; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
        long long ans = 0;
        for (int i = 0; i < (int)source.size(); i++) {
            int a = source[i] - 'a', b = target[i] - 'a';
            if (dist[a][b] >= inf / 2) return -1;
            ans += dist[a][b];
        }
        return ans;
    }
};
