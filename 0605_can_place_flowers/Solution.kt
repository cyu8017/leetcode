// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/


class Solution {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        var remain = n
        var i = 0
        while (i < flowerbed.size && remain > 0) {
            if (flowerbed[i] == 0
                && (i == 0 || flowerbed[i - 1] == 0)
                && (i == flowerbed.size - 1 || flowerbed[i + 1] == 0)
            ) {
                flowerbed[i] = 1
                remain--
            }
            i++
        }
        return remain == 0
    }
}
