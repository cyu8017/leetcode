// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int maxSameLengthRuns(std::string s) {
        std::unordered_map<int, int> cnt;
        int n = (int)s.size(), ans = 0;
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && s[j] == s[i]) j++;
            int m = j - i;
            ans = std::max(ans, ++cnt[m]);
            i = j;
        }
        return ans;
    }
};
