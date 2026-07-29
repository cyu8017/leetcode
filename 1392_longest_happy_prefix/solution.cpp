#include <string>
#include <vector>

class Solution {
public:
    std::string longestPrefix(std::string s) {
        int n = (int)s.size();
        if (!n) return "";
        std::vector<int> pi(n, 0);
        for (int i = 1; i < n; ++i) {
            int j = pi[i - 1];
            while (j && s[i] != s[j]) j = pi[j - 1];
            if (s[i] == s[j]) ++j;
            pi[i] = j;
        }
        return s.substr(0, pi.back());
    }
};
