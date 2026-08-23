// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

#include <vector>
#include <algorithm>

class Solution {
public:
    int largestCombination(std::vector<int>& candidates) {
        int ans = 0;
        for (int bit = 0; bit < 24; ++bit) {
            int cnt = 0;
            for (int x : candidates) if ((x >> bit) & 1) cnt++;
            ans = std::max(ans, cnt);
        }
        return ans;
    }
};
