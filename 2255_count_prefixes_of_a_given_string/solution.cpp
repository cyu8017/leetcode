// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

#include <vector>
#include <string>

class Solution {
public:
    int countPrefixes(std::vector<std::string>& words, std::string s) {
        int ans = 0;
        for (auto& w : words)
            if (w.size() <= s.size() && s.compare(0, w.size(), w) == 0) ans++;
        return ans;
    }
};
