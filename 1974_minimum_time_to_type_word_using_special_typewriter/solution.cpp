// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
#include <algorithm>
#include <cstdlib>
#include <string>

class Solution {
public:
    int minTimeToType(std::string word) {
        char cur = 'a';
        int ans = 0;
        for (char ch : word) {
            int d = std::abs(ch - cur);
            ans += std::min(d, 26 - d) + 1;
            cur = ch;
        }
        return ans;
    }
};
