// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

/**
 * @param {number[]} heights
 * @param {number} volume
 * @param {number} k
 * @return {number[]}
 */
var pourWater = function(heights, volume, k) {
    for (let v = 0; v < volume; v++) {
        let index = k;
        for (let i = k - 1; i >= 0; i--) {
            if (heights[i] > heights[index]) break;
            if (heights[i] < heights[index]) index = i;
        }
        if (index !== k) { heights[index]++; continue; }
        index = k;
        for (let i = k + 1; i < heights.length; i++) {
            if (heights[i] > heights[index]) break;
            if (heights[i] < heights[index]) index = i;
        }
        heights[index]++;
    }
    return heights;
};
