// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

#include <string>
#include <vector>

class Solution {
public:
    std::string decodeMessage(std::string key, std::string message) {
        std::vector<char> mp(26, 0);
        char next = 'a';
        for (char c : key) {
            if (c == ' ' || mp[c - 'a']) continue;
            mp[c - 'a'] = next++;
        }
        std::string out = message;
        for (char& c : out) {
            if (c != ' ') c = mp[c - 'a'];
        }
        return out;
    }
};
