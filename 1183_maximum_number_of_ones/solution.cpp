// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
        std::vector<int> counts;
        for (int r = 0; r < sideLength; ++r) {
            for (int c = 0; c < sideLength; ++c) {
                int rows = (height - r + sideLength - 1) / sideLength;
                int cols = (width - c + sideLength - 1) / sideLength;
                counts.push_back(rows * cols);
            }
        }
        std::sort(counts.rbegin(), counts.rend());
        int ans = 0;
        for (int i = 0; i < maxOnes; ++i) ans += counts[i];
        return ans;
    }
};
