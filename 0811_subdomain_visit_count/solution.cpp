// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> subdomainVisits(std::vector<std::string>& cpdomains) {
        std::unordered_map<std::string, int> counts;
        for (const auto& item : cpdomains) {
            auto space = item.find(' ');
            int count = std::stoi(item.substr(0, space));
            std::string domain = item.substr(space + 1);
            while (true) {
                counts[domain] += count;
                auto dot = domain.find('.');
                if (dot == std::string::npos) {
                    break;
                }
                domain = domain.substr(dot + 1);
            }
        }
        std::vector<std::string> ans;
        for (auto& [domain, count] : counts) {
            ans.push_back(std::to_string(count) + " " + domain);
        }
        return ans;
    }
};
