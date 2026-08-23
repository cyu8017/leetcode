// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
    using Graph = std::unordered_map<std::string, std::unordered_map<std::string, double>>;

    Graph buildRateGraph(std::vector<std::vector<std::string>>& pairs, std::vector<double>& rates) {
        Graph g;
        for (int i = 0; i < (int)pairs.size(); i++) {
            auto& a = pairs[i][0];
            auto& b = pairs[i][1];
            g[a][b] = rates[i];
            g[b][a] = 1.0 / rates[i];
        }
        return g;
    }

    std::unordered_map<std::string, double> bellman(const std::string& start,
        std::vector<std::vector<std::string>>& pairs, std::vector<double>& rates) {
        Graph g = buildRateGraph(pairs, rates);
        std::unordered_map<std::string, double> dist;
        dist[start] = 1.0;
        for (int it = 0; it < 100; it++) {
            bool updated = false;
            for (auto& [from, edges] : g) {
                if (!dist.count(from) || dist[from] == 0) continue;
                for (auto& [to, rate] : edges) {
                    double nv = dist[from] * rate;
                    if (!dist.count(to) || nv > dist[to]) {
                        dist[to] = nv;
                        updated = true;
                    }
                }
            }
            if (!updated) break;
        }
        return dist;
    }

public:
    double maxAmount(std::string initialCurrency, std::vector<std::vector<std::string>>& pairs1,
                     std::vector<double>& rates1, std::vector<std::vector<std::string>>& pairs2,
                     std::vector<double>& rates2) {
        auto amt1 = bellman(initialCurrency, pairs1, rates1);
        double ans = 1.0;
        Graph g2 = buildRateGraph(pairs2, rates2);
        for (auto& [c, a] : amt1) {
            if (a <= 0) continue;
            std::unordered_map<std::string, double> dist;
            dist[c] = a;
            bool updated = true;
            for (int it = 0; it < 100 && updated; it++) {
                updated = false;
                for (auto& [from, edges] : g2) {
                    if (!dist.count(from) || dist[from] == 0) continue;
                    for (auto& [to, rate] : edges) {
                        double nv = dist[from] * rate;
                        if (!dist.count(to) || nv > dist[to]) {
                            dist[to] = nv;
                            updated = true;
                        }
                    }
                }
            }
            if (dist.count(initialCurrency) && dist[initialCurrency] > ans)
                ans = dist[initialCurrency];
        }
        return ans;
    }
};
