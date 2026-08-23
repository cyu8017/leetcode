// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

#include <vector>

class Solution {
public:
    int captureForts(std::vector<int>& forts) {
        int ans = 0, prev = -1;
        for (int i = 0; i < (int)forts.size(); i++) {
            if (forts[i] != 0) {
                if (prev >= 0 && forts[prev] == -forts[i]) {
                    if (i - prev - 1 > ans) ans = i - prev - 1;
                }
                prev = i;
            }
        }
        return ans;
    }
};
