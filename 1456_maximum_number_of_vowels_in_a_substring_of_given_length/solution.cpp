#include <algorithm>
#include <string>

class Solution {
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
public:
    int maxVowels(std::string s, int k) {
        int cur = 0;
        for (int i = 0; i < k; ++i) cur += isVowel(s[i]);
        int ans = cur;
        for (int i = k; i < (int)s.size(); ++i) {
            cur += isVowel(s[i]) - isVowel(s[i - k]);
            ans = std::max(ans, cur);
        }
        return ans;
    }
};
