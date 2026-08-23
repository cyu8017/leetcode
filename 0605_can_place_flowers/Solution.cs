// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) return true;
        for (int i = 0; i < flowerbed.Length; ++i) {
            if (flowerbed[i] == 1) continue;
            bool leftEmpty = i == 0 || flowerbed[i - 1] == 0;
            bool rightEmpty = i == flowerbed.Length - 1 || flowerbed[i + 1] == 0;
            if (leftEmpty && rightEmpty) {
                flowerbed[i] = 1;
                --n;
                if (n == 0) return true;
            }
        }
        return false;
    }
}
