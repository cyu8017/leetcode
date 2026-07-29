// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int numBusesToDestination(std::vector<std::vector<int>>& routes, int source,
                              int target) {
        if (source == target) {
            return 0;
        }
        std::unordered_map<int, std::vector<int>> stopToBuses;
        for (int bus = 0; bus < static_cast<int>(routes.size()); ++bus) {
            for (int stop : routes[bus]) {
                stopToBuses[stop].push_back(bus);
            }
        }
        std::queue<std::pair<int, int>> queue;
        queue.push({source, 0});
        std::unordered_set<int> seenStops{source};
        std::unordered_set<int> seenBuses;
        while (!queue.empty()) {
            auto [stop, busesTaken] = queue.front();
            queue.pop();
            for (int bus : stopToBuses[stop]) {
                if (seenBuses.count(bus)) {
                    continue;
                }
                seenBuses.insert(bus);
                for (int nxt : routes[bus]) {
                    if (nxt == target) {
                        return busesTaken + 1;
                    }
                    if (!seenStops.count(nxt)) {
                        seenStops.insert(nxt);
                        queue.push({nxt, busesTaken + 1});
                    }
                }
            }
        }
        return -1;
    }
};
