// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

/**
 * Definition for an infinite stream.
 * class InfiniteStream {
 * public:
 *     InfiniteStream(vector<int> bits);
 *     int next();
 * };
 */

#include <vector>

class Solution {
    static std::vector<int> getLPS(const std::vector<int>& pattern) {
        int n = (int)pattern.size();
        std::vector<int> lps(n, 0);
        int j = 0;
        for (int i = 1; i < n; i++) {
            while (j > 0 && pattern[j] != pattern[i]) j = lps[j - 1];
            if (pattern[i] == pattern[j]) {
                j++;
                lps[i] = j;
            }
        }
        return lps;
    }
public:
    int findPattern(InfiniteStream* stream, std::vector<int>& pattern) {
        auto lps = getLPS(pattern);
        int i = 0, j = 0, bit = 0;
        bool readNext = false;
        while (true) {
            if (!readNext) {
                bit = stream->next();
                readNext = true;
            }
            if (bit == pattern[j]) {
                i++;
                readNext = false;
                j++;
                if (j == (int)pattern.size()) return i - j;
            } else if (j > 0) {
                j = lps[j - 1];
            } else {
                i++;
                readNext = false;
            }
        }
    }
};
