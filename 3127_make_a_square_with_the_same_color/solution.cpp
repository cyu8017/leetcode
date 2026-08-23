// LeetCode 3127 - Make a Square with the Same Color
// https://leetcode.com/problems/make-a-square-with-the-same-color/

#include <vector>

class Solution {
public:
    bool canMakeSquare(std::vector<std::vector<char>>& grid) {
        int dirs[5] = {0, 0, 1, 1, 0};
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                int cnt1 = 0, cnt2 = 0;
                for (int k = 0; k < 4; k++) {
                    int x = i + dirs[k], y = j + dirs[k + 1];
                    if (grid[x][y] == 'W') cnt1++;
                    else cnt2++;
                }
                if (cnt1 != cnt2) return true;
            }
        }
        return false;
    }
};
