// LeetCode 0332 - Reconstruct Itinerary
// https://leetcode.com/problems/reconstruct-itinerary/

#include <algorithm>
#include <functional>
#include <map>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> findItinerary(std::vector<std::vector<std::string>>& tickets) {
        std::map<std::string, std::vector<std::string>> targets;
        for (const auto& ticket : tickets) {
            targets[ticket[0]].push_back(ticket[1]);
        }
        for (auto& entry : targets) {
            std::sort(entry.second.begin(), entry.second.end());
        }

        std::vector<std::string> route;
        std::function<void(const std::string&)> visit = [&](const std::string& airport) {
            while (!targets[airport].empty()) {
                std::string next = targets[airport].back();
                targets[airport].pop_back();
                visit(next);
            }
            route.push_back(airport);
        };

        visit("JFK");
        std::reverse(route.begin(), route.end());
        return route;
    }
};
