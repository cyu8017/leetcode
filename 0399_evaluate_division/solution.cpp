// LeetCode 0399 - Evaluate Division
// https://leetcode.com/problems/evaluate-division/

#include <functional>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<double> calcEquation(
        std::vector<std::vector<std::string>>& equations,
        std::vector<double>& values,
        std::vector<std::vector<std::string>>& queries
    ) {
        std::unordered_map<std::string, std::unordered_map<std::string, double>> graph;

        for (size_t index = 0; index < equations.size(); ++index) {
            const std::string& dividend = equations[index][0];
            const std::string& divisor = equations[index][1];
            graph[dividend][divisor] = values[index];
            graph[divisor][dividend] = 1.0 / values[index];
        }

        std::function<double(const std::string&, const std::string&, std::unordered_set<std::string>&)> dfs;
        dfs = [&](const std::string& start, const std::string& end,
                  std::unordered_set<std::string>& visited) -> double {
            if (!graph.count(start) || !graph.count(end)) {
                return -1.0;
            }
            if (start == end) {
                return 1.0;
            }
            visited.insert(start);
            for (const auto& entry : graph[start]) {
                if (visited.count(entry.first)) {
                    continue;
                }
                double result = dfs(entry.first, end, visited);
                if (result != -1.0) {
                    return entry.second * result;
                }
            }
            return -1.0;
        };

        std::vector<double> answers;
        for (const auto& query : queries) {
            std::unordered_set<std::string> visited;
            answers.push_back(dfs(query[0], query[1], visited));
        }
        return answers;
    }
};
