// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

#include <stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    if (n == 0) {
        return true;
    }
    for (int i = 0; i < flowerbedSize; i++) {
        if (flowerbed[i] == 1) {
            continue;
        }
        int leftEmpty = i == 0 || flowerbed[i - 1] == 0;
        int rightEmpty = i == flowerbedSize - 1 || flowerbed[i + 1] == 0;
        if (leftEmpty && rightEmpty) {
            flowerbed[i] = 1;
            n--;
            if (n == 0) {
                return true;
            }
        }
    }
    return false;
}
