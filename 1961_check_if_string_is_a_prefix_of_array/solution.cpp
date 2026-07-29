// LeetCode 1961 - Check If String Is a Prefix of Array
#include <string>
#include <vector>

class Solution {
public:
    bool isPrefixString(std::string s, std::vector<std::string>& words) {
        std::string cur;
        for (auto& w : words) {
            cur += w;
            if (cur == s) return true;
            if (cur.size() > s.size() || s.compare(0, cur.size(), cur) != 0) return false;
        }
        return false;
    }
};
