// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> countMentions(int numberOfUsers, std::vector<std::vector<std::string>>& events) {
        std::stable_sort(events.begin(), events.end(), [](const auto& a, const auto& b) {
            int ti = std::stoi(a[1]), tj = std::stoi(b[1]);
            if (ti != tj) return ti < tj;
            return a[0] > b[0];
        });
        std::vector<char> online(numberOfUsers, 1);
        std::vector<int> offlineUntil(numberOfUsers, 0);
        std::vector<int> ans(numberOfUsers, 0);
        for (auto& e : events) {
            int t = std::stoi(e[1]);
            for (int i = 0; i < numberOfUsers; i++) {
                if (!online[i] && offlineUntil[i] <= t) online[i] = 1;
            }
            if (e[0] == "OFFLINE") {
                int id = std::stoi(e[2]);
                online[id] = 0;
                offlineUntil[id] = t + 60;
            } else {
                const std::string& msg = e[2];
                if (msg == "ALL") {
                    for (int i = 0; i < numberOfUsers; i++) ans[i]++;
                } else if (msg == "HERE") {
                    for (int i = 0; i < numberOfUsers; i++) if (online[i]) ans[i]++;
                } else {
                    std::istringstream iss(msg);
                    std::string part;
                    while (iss >> part) {
                        int id = std::stoi(part.substr(2));
                        ans[id]++;
                    }
                }
            }
        }
        return ans;
    }
};
