// LeetCode 0115 - Distinct Subsequences
#include <string>
#include <vector>
class Solution { public: int numDistinct(std::string s, std::string t) {
    std::vector<unsigned long long> dp(t.size() + 1); dp[0] = 1;
    for (char a : s) for (int j = (int)t.size(); j; --j)
        if (a == t[j - 1]) dp[j] += dp[j - 1];
    return (int)dp.back();
} };