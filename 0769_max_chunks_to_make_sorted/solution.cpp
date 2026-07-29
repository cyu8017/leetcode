// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxChunksToSorted(std::vector<int>& arr) {
        int chunks = 0;
        int maxSoFar = 0;
        for (int i = 0; i < static_cast<int>(arr.size()); ++i) {
            maxSoFar = std::max(maxSoFar, arr[i]);
            if (maxSoFar == i) {
                ++chunks;
            }
        }
        return chunks;
    }
};
