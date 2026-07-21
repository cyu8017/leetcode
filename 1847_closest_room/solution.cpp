// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

#include <algorithm>
#include <cstdlib>
#include <limits>
#include <set>
#include <vector>

class Solution {
public:
    std::vector<int> closestRoom(std::vector<std::vector<int>>& rooms, std::vector<std::vector<int>>& queries) {
        std::sort(rooms.begin(), rooms.end(), [](const auto& a, const auto& b) {
            return a[1] < b[1];
        });
        std::vector<std::pair<int, std::vector<int>>> indexed;
        indexed.reserve(queries.size());
        for (int i = 0; i < static_cast<int>(queries.size()); ++i) {
            indexed.push_back({i, queries[i]});
        }
        std::sort(indexed.begin(), indexed.end(), [](const auto& a, const auto& b) {
            return a.second[1] > b.second[1];
        });

        std::set<int> availableIds;
        int roomIndex = static_cast<int>(rooms.size()) - 1;
        std::vector<int> answer(queries.size(), -1);

        for (const auto& [queryIndex, query] : indexed) {
            int preferred = query[0];
            int minSize = query[1];
            while (roomIndex >= 0 && rooms[roomIndex][1] >= minSize) {
                availableIds.insert(rooms[roomIndex][0]);
                --roomIndex;
            }
            if (availableIds.empty()) {
                continue;
            }
            auto it = availableIds.lower_bound(preferred);
            int bestId = -1;
            int bestDist = std::numeric_limits<int>::max();
            if (it != availableIds.end()) {
                int roomId = *it;
                int dist = std::abs(roomId - preferred);
                if (dist < bestDist || (dist == bestDist && roomId < bestId)) {
                    bestId = roomId;
                    bestDist = dist;
                }
            }
            if (it != availableIds.begin()) {
                --it;
                int roomId = *it;
                int dist = std::abs(roomId - preferred);
                if (dist < bestDist || (dist == bestDist && roomId < bestId)) {
                    bestId = roomId;
                }
            }
            answer[queryIndex] = bestId;
        }
        return answer;
    }
};
