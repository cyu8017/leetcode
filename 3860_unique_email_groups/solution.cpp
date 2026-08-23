// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

#include <cctype>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int uniqueEmailGroups(std::vector<std::string>& emails) {
        std::unordered_set<std::string> st;
        for (auto& email : emails) {
            auto at = email.find('@');
            std::string local = email.substr(0, at);
            std::string domain = email.substr(at + 1);
            auto plus = local.find('+');
            if (plus != std::string::npos) local = local.substr(0, plus);
            std::string cleaned;
            for (char c : local) if (c != '.') cleaned.push_back(std::tolower(static_cast<unsigned char>(c)));
            for (char& c : domain) c = std::tolower(static_cast<unsigned char>(c));
            st.insert(cleaned + domain);
        }
        return (int)st.size();
    }
};
