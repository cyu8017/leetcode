// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> getWordsInLongestSubsequence(std::vector<std::string>& words, std::vector<int>& groups) {
        int n = (int)words.size();
        std::vector<int> dp(n, 1), prev(n, -1);
        auto hamming = [](const std::string& a, const std::string& b) {
            if (a.size() != b.size()) return 100;
            int d = 0;
            for (int i = 0; i < (int)a.size(); i++) if (a[i] != b[i]) d++;
            return d;
        };
        int best = 1, bestI = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (groups[i] != groups[j] && hamming(words[i], words[j]) == 1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > best) {
                best = dp[i];
                bestI = i;
            }
        }
        std::vector<std::string> path;
        for (int i = bestI; i != -1; i = prev[i]) path.push_back(words[i]);
        std::reverse(path.begin(), path.end());
        return path;
    }
};
