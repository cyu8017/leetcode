// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

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
public:
    int findPattern(InfiniteStream* stream, std::vector<int>& pattern) {
        int a = 0, b = 0;
        int m = (int)pattern.size();
        int half = m >> 1;
        int mask1 = (1 << half) - 1;
        int mask2 = (1 << (m - half)) - 1;
        for (int i = 0; i < half; i++) a |= pattern[i] << (half - 1 - i);
        for (int i = half; i < m; i++) b |= pattern[i] << (m - 1 - i);
        int x = 0, y = 0;
        for (int i = 1; ; i++) {
            int v = stream->next();
            y = y << 1 | v;
            v = (y >> (m - half)) & 1;
            y &= mask2;
            x = x << 1 | v;
            x &= mask1;
            if (i >= m && a == x && b == y) return i - m;
        }
    }
};
