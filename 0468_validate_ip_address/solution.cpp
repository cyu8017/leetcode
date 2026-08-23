// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

#include <cctype>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
    bool isIPv4(const std::string& address) {
        std::vector<std::string> parts;
        std::string current;
        for (char ch : address) {
            if (ch == '.') {
                parts.push_back(current);
                current.clear();
            } else {
                current.push_back(ch);
            }
        }
        parts.push_back(current);
        if (parts.size() != 4) {
            return false;
        }
        for (const std::string& part : parts) {
            if (part.empty() || part.size() > 3) {
                return false;
            }
            if (part.size() > 1 && part[0] == '0') {
                return false;
            }
            if (!std::all_of(part.begin(), part.end(), ::isdigit)) {
                return false;
            }
            int value = std::stoi(part);
            if (value > 255) {
                return false;
            }
        }
        return true;
    }

    bool isIPv6(const std::string& address) {
        std::vector<std::string> parts;
        std::string current;
        for (char ch : address) {
            if (ch == ':') {
                parts.push_back(current);
                current.clear();
            } else {
                current.push_back(ch);
            }
        }
        parts.push_back(current);
        if (parts.size() != 8) {
            return false;
        }
        const std::unordered_set<char> hexDigits = {
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F',
        };
        for (const std::string& part : parts) {
            if (part.empty() || part.size() > 4) {
                return false;
            }
            for (char ch : part) {
                if (!hexDigits.count(ch)) {
                    return false;
                }
            }
        }
        return true;
    }

public:
    std::string validIPAddress(std::string queryIP) {
        if (isIPv4(queryIP)) {
            return "IPv4";
        }
        if (isIPv6(queryIP)) {
            return "IPv6";
        }
        return "Neither";
    }
};
