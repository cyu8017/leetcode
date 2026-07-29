#include <algorithm>
#include <string>

class Solution {
public:
    int numberOfSubstrings(std::string s) {
        int last[3] = {-1, -1, -1}, ans = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            last[s[i] - 'a'] = i;
            ans += 1 + std::min({last[0], last[1], last[2]});
        }
        return ans;
    }
};
