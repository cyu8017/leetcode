// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

#include <string>

class Solution {
public:
    std::string minWindow(std::string s1, std::string s2) {
        int m = static_cast<int>(s1.size());
        int n = static_cast<int>(s2.size());
        std::string best;
        int i = 0;
        while (i < m) {
            int j = 0;
            int k = i;
            while (k < m && j < n) {
                if (s1[k] == s2[j]) {
                    ++j;
                }
                ++k;
            }
            if (j < n) {
                break;
            }
            int end = k - 1;
            j = n - 1;
            k = end;
            while (j >= 0) {
                if (s1[k] == s2[j]) {
                    --j;
                }
                --k;
            }
            int start = k + 1;
            if (best.empty() || end - start + 1 < static_cast<int>(best.size())) {
                best = s1.substr(start, end - start + 1);
            }
            i = start + 1;
        }
        return best;
    }
};
