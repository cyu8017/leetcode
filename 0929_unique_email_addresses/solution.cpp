// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int numUniqueEmails(std::vector<std::string>& emails) {
        std::unordered_set<std::string> normalized;
        for (const auto& email : emails) {
            auto at = email.find('@');
            std::string local = email.substr(0, at);
            std::string domain = email.substr(at);
            auto plus = local.find('+');
            if (plus != std::string::npos) local = local.substr(0, plus);
            std::string cleaned;
            for (char c : local) if (c != '.') cleaned.push_back(c);
            normalized.insert(cleaned + domain);
        }
        return (int)normalized.size();
    }
};
