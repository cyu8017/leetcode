// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

#include <vector>

class Solution {
public:
    bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {
        if (n == 0) {
            return true;
        }
        for (int i = 0; i < static_cast<int>(flowerbed.size()); ++i) {
            if (flowerbed[i] == 1) {
                continue;
            }
            const bool leftEmpty = i == 0 || flowerbed[i - 1] == 0;
            const bool rightEmpty =
                i == static_cast<int>(flowerbed.size()) - 1 || flowerbed[i + 1] == 0;
            if (leftEmpty && rightEmpty) {
                flowerbed[i] = 1;
                --n;
                if (n == 0) {
                    return true;
                }
            }
        }
        return false;
    }
};
