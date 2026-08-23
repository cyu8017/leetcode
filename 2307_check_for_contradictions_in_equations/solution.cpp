// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>
#include <functional>

class Solution {
public:
    bool checkContradictions(std::vector<std::vector<std::string>>& equations, std::vector<double>& values) {
        std::unordered_map<std::string, std::string> parent;
        std::unordered_map<std::string, double> weight;
        std::function<std::string(const std::string&)> find = [&](const std::string& x) -> std::string {
            if (!parent.count(x)) { parent[x] = x; weight[x] = 1; return x; }
            if (parent[x] != x) {
                std::string p = find(parent[x]);
                weight[x] *= weight[parent[x]];
                parent[x] = p;
            }
            return parent[x];
        };
        for (size_t i = 0; i < equations.size(); ++i) {
            const std::string& a = equations[i][0], &b = equations[i][1];
            std::string ra = find(a), rb = find(b);
            if (ra == rb) {
                if (std::fabs(weight[a] / weight[b] - values[i]) > 1e-5) return true;
            } else {
                parent[ra] = rb;
                weight[ra] = values[i] * weight[b] / weight[a];
            }
        }
        return false;
    }
};
