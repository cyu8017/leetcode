// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> accountsMerge(std::vector<std::vector<std::string>>& accounts) {
        std::unordered_map<std::string, std::string> parent;
        std::unordered_map<std::string, std::string> emailName;

        auto find = [&](std::string x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        auto unite = [&](const std::string& a, const std::string& b) {
            parent[find(a)] = find(b);
        };

        for (const auto& account : accounts) {
            const std::string& name = account[0];
            const std::string& first = account[1];
            for (size_t i = 1; i < account.size(); ++i) {
                const std::string& email = account[i];
                if (!parent.count(email)) {
                    parent[email] = email;
                }
                emailName[email] = name;
                unite(first, email);
            }
        }

        std::unordered_map<std::string, std::vector<std::string>> groups;
        for (const auto& [email, _] : parent) {
            groups[find(email)].push_back(email);
        }

        std::vector<std::vector<std::string>> result;
        for (auto& [_, emails] : groups) {
            std::sort(emails.begin(), emails.end());
            std::vector<std::string> row;
            row.push_back(emailName[emails[0]]);
            row.insert(row.end(), emails.begin(), emails.end());
            result.push_back(std::move(row));
        }
        return result;
    }
};
