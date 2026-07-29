// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
#include <string>
#include <vector>

class Solution {
public:
    int numOfStrings(std::vector<std::string>& patterns, std::string word) {
        int ans = 0;
        for (auto& p : patterns) if (word.find(p) != std::string::npos) ans++;
        return ans;
    }
};
