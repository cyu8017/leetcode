// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

#include <algorithm>
#include <string>

class Solution {
public:
    int minimumRecolors(std::string blocks, int k) {
        int white = 0;
        for (int i = 0; i < k; i++) if (blocks[i] == 'W') white++;
        int ans = white;
        for (int i = k; i < (int)blocks.size(); i++) {
            if (blocks[i] == 'W') white++;
            if (blocks[i - k] == 'W') white--;
            ans = std::min(ans, white);
        }
        return ans;
    }
};
