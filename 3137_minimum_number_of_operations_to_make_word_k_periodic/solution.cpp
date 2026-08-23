// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int minimumOperationsToMakeKPeriodic(std::string word, int k) {
        std::unordered_map<std::string, int> cnt;
        int n = (int)word.size(), mx = 0;
        for (int i = 0; i < n; i += k) {
            std::string s = word.substr(i, k);
            mx = std::max(mx, ++cnt[s]);
        }
        return n / k - mx;
    }
};
