// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> findHighAccessEmployees(std::vector<std::vector<std::string>>& accessTimes) {
        std::unordered_map<std::string, std::vector<int>> m;
        for (auto& a : accessTimes) {
            const std::string& name = a[0];
            const std::string& t = a[1];
            int hh = (t[0] - '0') * 10 + (t[1] - '0');
            int mm = (t[2] - '0') * 10 + (t[3] - '0');
            m[name].push_back(hh * 60 + mm);
        }
        std::vector<std::string> ans;
        for (auto& [name, times] : m) {
            std::sort(times.begin(), times.end());
            for (int i = 0; i + 2 < (int)times.size(); i++) {
                if (times[i + 2] - times[i] < 60) {
                    ans.push_back(name);
                    break;
                }
            }
        }
        std::sort(ans.begin(), ans.end());
        return ans;
    }
};
