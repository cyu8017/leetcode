// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimumBeautifulSubstrings(std::string s) {
        int n = (int)s.size();
        std::unordered_set<std::string> pow5;
        for (long long x = 1; ; x *= 5) {
            std::string b;
            long long t = x;
            while (t) { b.push_back(char('0' + (t & 1))); t >>= 1; }
            std::reverse(b.begin(), b.end());
            if (b.empty()) b = "0";
            if ((int)b.size() > n) break;
            pow5.insert(b);
        }
        const int INF = 1 << 30;
        std::vector<int> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == INF || s[i] == '0') continue;
            for (int j = i + 1; j <= n; j++) {
                if (pow5.count(s.substr(i, j - i))) {
                    dp[j] = std::min(dp[j], dp[i] + 1);
                }
            }
        }
        return dp[n] == INF ? -1 : dp[n];
    }
};
