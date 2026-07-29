// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int findLongestChain(std::vector<std::vector<int>>& pairs) {
        std::sort(pairs.begin(), pairs.end(),
                  [](const std::vector<int>& a, const std::vector<int>& b) {
                      return a[1] < b[1];
                  });
        int length = 0;
        int currentEnd = INT_MIN;
        for (const auto& pair : pairs) {
            if (pair[0] > currentEnd) {
                ++length;
                currentEnd = pair[1];
            }
        }
        return length;
    }
};
