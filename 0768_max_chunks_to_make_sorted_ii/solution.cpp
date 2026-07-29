// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxChunksToSorted(std::vector<int>& arr) {
        int n = static_cast<int>(arr.size());
        std::vector<int> maxLeft(n), minRight(n);
        maxLeft[0] = arr[0];
        for (int i = 1; i < n; ++i) {
            maxLeft[i] = std::max(maxLeft[i - 1], arr[i]);
        }
        minRight[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            minRight[i] = std::min(minRight[i + 1], arr[i]);
        }
        int chunks = 1;
        for (int i = 0; i < n - 1; ++i) {
            if (maxLeft[i] <= minRight[i + 1]) {
                ++chunks;
            }
        }
        return chunks;
    }
};
