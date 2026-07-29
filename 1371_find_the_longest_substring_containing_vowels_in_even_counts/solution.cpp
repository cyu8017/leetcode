#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int findTheLongestSubstring(std::string s) {
        std::unordered_map<int, int> first{{0, -1}};
        int mask = 0, ans = 0;
        std::string vowels = "aeiou";
        for (int i = 0; i < (int)s.size(); ++i) {
            auto pos = vowels.find(s[i]);
            if (pos != std::string::npos) mask ^= 1 << (int)pos;
            if (first.count(mask)) ans = std::max(ans, i - first[mask]);
            else first[mask] = i;
        }
        return ans;
    }
};
