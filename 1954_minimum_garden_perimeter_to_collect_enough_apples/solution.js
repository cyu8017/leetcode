// LeetCode 1954 - Minimum Garden Perimeter to Collect Enough Apples
// https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

/**
 * @param {number} neededApples
 * @return {number}
 */
var minimumPerimeter = function(neededApples) {
    let lo = 1, hi = 100000;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        const apples = 2 * mid * (mid + 1) * (2 * mid + 1);
        if (apples >= neededApples) hi = mid;
        else lo = mid + 1;
    }
    return 8 * lo;
};
