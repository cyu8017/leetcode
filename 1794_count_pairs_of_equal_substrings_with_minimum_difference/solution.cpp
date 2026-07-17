// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

#include <algorithm>
#include <climits>
#include <string>

class Solution {
public:
    long long countQuadruples(std::string firstString, std::string secondString) {
        int first[26], lastF[26], lastS[26];
        std::fill(first, first + 26, -1);
        std::fill(lastF, lastF + 26, -1);
        std::fill(lastS, lastS + 26, -1);
        for (int i = 0; i < (int)firstString.size(); i++) {
            int c = firstString[i] - 'a';
            if (first[c] == -1) first[c] = i;
            lastF[c] = i;
        }
        for (int i = 0; i < (int)secondString.size(); i++) {
            lastS[secondString[i] - 'a'] = i;
        }
        long long best = LLONG_MAX;
        for (int c = 0; c < 26; c++) {
            if (first[c] != -1 && lastS[c] != -1) {
                best = std::min(best, (long long)lastF[c] - lastS[c]);
            }
        }
        if (best == LLONG_MAX) return 0;
        long long ans = 0;
        for (int c = 0; c < 26; c++) {
            if (first[c] == -1 || lastS[c] == -1 || lastF[c] - lastS[c] != best) continue;
            long long iCount = 0;
            for (int k = first[c]; k <= lastF[c]; k++) {
                if (firstString[k] - 'a' == c) iCount++;
            }
            long long aCount = 0;
            for (int k = 0; k <= lastS[c]; k++) {
                if (secondString[k] - 'a' == c) aCount++;
            }
            ans += iCount * aCount;
        }
        return ans;
    }
};
