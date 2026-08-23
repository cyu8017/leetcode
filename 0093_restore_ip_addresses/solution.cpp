// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> restoreIpAddresses(std::string s) {
        std::vector<std::string> result;
        std::vector<std::string> path;
        backtrack(s, 0, path, result);
        return result;
    }

private:
    void backtrack(
        const std::string& s,
        size_t start,
        std::vector<std::string>& path,
        std::vector<std::string>& result
    ) {
        if (path.size() == 4) {
            if (start == s.size()) {
                result.push_back(path[0] + "." + path[1] + "." + path[2] + "." + path[3]);
            }
            return;
        }

        for (size_t length = 1; length <= 3; ++length) {
            if (start + length > s.size()) {
                break;
            }
            std::string part = s.substr(start, length);
            if ((part[0] == '0' && part.size() > 1) || std::stoi(part) > 255) {
                continue;
            }
            path.push_back(part);
            backtrack(s, start + length, path, result);
            path.pop_back();
        }
    }
};
