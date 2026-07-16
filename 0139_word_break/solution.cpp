// LeetCode 0139 - Word Break
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
class Solution { public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> words(wordDict.begin(), wordDict.end());
        vector<bool> dp(s.size() + 1); dp[0] = true;
        for (int i = 1; i <= s.size(); ++i)
            for (int j = 0; j < i; ++j)
                if (dp[j] && words.count(s.substr(j, i - j))) { dp[i] = true; break; }
        return dp[s.size()];
    }
};