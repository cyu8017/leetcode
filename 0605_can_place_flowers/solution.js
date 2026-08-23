// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    if (n === 0) return true;
    for (let i = 0; i < flowerbed.length; ++i) {
        if (flowerbed[i] === 1) continue;
        const leftEmpty = i === 0 || flowerbed[i - 1] === 0;
        const rightEmpty = i === flowerbed.length - 1 || flowerbed[i + 1] === 0;
        if (leftEmpty && rightEmpty) {
            flowerbed[i] = 1;
            --n;
            if (n === 0) return true;
        }
    }
    return false;
};
