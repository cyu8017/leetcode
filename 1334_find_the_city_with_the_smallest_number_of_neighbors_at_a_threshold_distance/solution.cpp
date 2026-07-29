#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int findTheCity(int n, std::vector<std::vector<int>>& edges, int distanceThreshold) {
        const long long inf = (long long)1e15;
        std::vector<std::vector<long long>> dist(n, std::vector<long long>(n, inf));
        for (int i = 0; i < n; ++i) dist[i][i] = 0;
        for (auto& e : edges) {
            dist[e[0]][e[1]] = dist[e[1]][e[0]] = e[2];
        }
        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
        int bestCity = 0, bestCount = INT_MAX;
        for (int city = 0; city < n; ++city) {
            int count = 0;
            for (int j = 0; j < n; ++j)
                if (dist[city][j] <= distanceThreshold) ++count;
            if (count < bestCount || (count == bestCount && city > bestCity)) {
                bestCount = count;
                bestCity = city;
            }
        }
        return bestCity;
    }
};
