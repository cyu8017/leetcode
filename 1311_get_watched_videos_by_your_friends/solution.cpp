#include <algorithm>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::string> watchedVideosByFriends(std::vector<std::vector<std::string>>& watchedVideos,
                                                    std::vector<std::vector<int>>& friends, int id, int level) {
        std::queue<std::pair<int, int>> q;
        std::unordered_set<int> seen{id};
        q.push({id, 0});
        std::vector<int> people;
        while (!q.empty()) {
            auto [person, distance] = q.front();
            q.pop();
            if (distance == level) {
                people.push_back(person);
                continue;
            }
            for (int friendId : friends[person]) {
                if (!seen.count(friendId)) {
                    seen.insert(friendId);
                    q.push({friendId, distance + 1});
                }
            }
        }
        std::unordered_map<std::string, int> counts;
        for (int person : people)
            for (auto& video : watchedVideos[person]) ++counts[video];
        std::vector<std::string> answer;
        for (auto& [video, _] : counts) answer.push_back(video);
        std::sort(answer.begin(), answer.end(), [&](const std::string& a, const std::string& b) {
            if (counts[a] != counts[b]) return counts[a] < counts[b];
            return a < b;
        });
        return answer;
    }
};
