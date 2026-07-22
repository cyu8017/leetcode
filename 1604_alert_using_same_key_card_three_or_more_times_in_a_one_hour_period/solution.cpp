// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> alertNames(std::vector<std::string>& keyName, std::vector<std::string>& keyTime) {
        std::unordered_map<std::string, std::vector<int>> times;
        for (size_t i = 0; i < keyName.size(); ++i) {
            const int h = std::stoi(keyTime[i].substr(0, 2));
            const int m = std::stoi(keyTime[i].substr(3, 2));
            times[keyName[i]].push_back(h * 60 + m);
        }
        std::vector<std::string> ans;
        for (auto& [name, a] : times) {
            std::sort(a.begin(), a.end());
            for (size_t i = 0; i + 2 < a.size(); ++i) {
                if (a[i + 2] - a[i] <= 60) {
                    ans.push_back(name);
                    break;
                }
            }
        }
        std::sort(ans.begin(), ans.end());
        return ans;
    }
};
