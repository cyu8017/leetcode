// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> mostVisitedPattern(std::vector<std::string>& username,
                                                std::vector<int>& timestamp,
                                                std::vector<std::string>& website) {
        std::unordered_map<std::string, std::vector<std::pair<int, std::string>>> visits;
        for (size_t i = 0; i < username.size(); ++i)
            visits[username[i]].emplace_back(timestamp[i], website[i]);
        std::map<std::tuple<std::string, std::string, std::string>, int> scores;
        for (auto& [user, list] : visits) {
            std::sort(list.begin(), list.end());
            std::vector<std::string> sites;
            for (auto& [t, site] : list) sites.push_back(site);
            std::set<std::tuple<std::string, std::string, std::string>> patterns;
            int m = static_cast<int>(sites.size());
            for (int i = 0; i < m; ++i)
                for (int j = i + 1; j < m; ++j)
                    for (int k = j + 1; k < m; ++k)
                        patterns.emplace(sites[i], sites[j], sites[k]);
            for (const auto& p : patterns) ++scores[p];
        }
        std::tuple<std::string, std::string, std::string> best;
        int bestCount = -1;
        for (const auto& [pattern, count] : scores) {
            if (count > bestCount || (count == bestCount && pattern < best)) {
                bestCount = count;
                best = pattern;
            }
        }
        return {std::get<0>(best), std::get<1>(best), std::get<2>(best)};
    }
};
